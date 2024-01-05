"""
_dremio_connection.py


This code will allow a user to instantiate an object that can access the Dremio API via SQL queries

"""
import os
from pyarrow import flight
from dotenv import load_dotenv


class DremioClientAuthMiddlewareFactory(flight.ClientMiddlewareFactory):
    """A factory that creates DremioClientAuthMiddleware(s)."""

    def __init__(self):
        self.call_credential = []

    def start_call(self, info):
        return DremioClientAuthMiddleware(self)

    def set_call_credential(self, call_credential):
        self.call_credential = call_credential


class DremioClientAuthMiddleware(flight.ClientMiddleware):
    """
    A ClientMiddleware that extracts the bearer token from 
    the authorization header returned by the Dremio 
    Flight Server Endpoint.
    Parameters
    ----------
    factory : ClientHeaderAuthMiddlewareFactory
        The factory to set call credentials if an
        authorization header with bearer token is
        returned by the Dremio server.
    """

    def __init__(self, factory):
        self.factory = factory

    def received_headers(self, headers):
        auth_header_key = 'authorization'
        authorization_header = []
        for key in headers:
            if key.lower() == auth_header_key: authorization_header = headers.get(auth_header_key)
        self.factory.set_call_credential([
            b'authorization', authorization_header[0].encode("utf-8")])


class DremioAPI(object):
     """Object to simplify reading from Dremio (CDSI's SQL engine)."""
    def __init__(
        self, 
        *,
        fname_env: str, 
        env_key_user: Optional[str] = 'USER', 
        env_key_pw: Optional[str] = 'PW',
        scheme: Optional[str] = "grpc+tcp",
        hostname: Optional[str] = "tlvidreamcord1",
        flightport: Optional[int] = 32010
    ):
        """Initialization
        
        Args:
            fname_env: Environment file with username and pw
            env_key_user: Key term to identify the username in fname_env
            env_key_pw: Key term to identify the password in fname_env
            scheme: The connection scheme used
            hostname: Server hostname
            flightport: Port number
            
        """
        
        self._df = None
        self._scheme = scheme
        self._hostname = hostname
        self._flightport = flightport
        
        load_dotenv(fname_env)
        self._authenticate(
            user=os.getenv(env_key_user), 
            pw=os.getenv(env_key_pw)
        )
        
    def return_data(self):
        """Return data queried from Dremio in a Pandas dataframe
            
        Returns:
            df
            
        """
        df = self._df
        
        return df
            
    def _authenticate(self, user, pw):
        scheme = self._scheme
        hostname = self._hostname
        flightport = self._flightport
        connection_args = {}
        # Two WLM settings can be provided upon initial authentication 
        # with the Dremio Server Flight Endpoint:
        # - routing-tag
        # - routing queue
        initial_options = flight.FlightCallOptions(headers=[
            (b'routing-tag', b'test-routing-tag'),
            (b'routing-queue', b'Low Cost User Queries')
        ])
        client_auth_middleware = DremioClientAuthMiddlewareFactory()
        client = flight.FlightClient(f"{scheme}://{hostname}:{flightport}", middleware=[client_auth_middleware], **connection_args)
        bearer_token = client.authenticate_basic_token(
            user, 
            pw, 
            initial_options
        )
        print('[INFO] Authentication was successful')
        
        self._client = client
        self._bearer_token = bearer_token
        
    def query_data(self, sql):
        """Query Dremio with SQL string
        
        Args:
            sql: SQL string used to query Dremio
            
        Returns:
            df_output
            
        """
        client = self._client
        bearer_token = self._bearer_token
        # Get table from our dicom segments
        flight_desc = flight.FlightDescriptor.for_command(sql)
        options = flight.FlightCallOptions(headers=[bearer_token])
        schema = client.get_schema(flight_desc, options)

        flight_info = client.get_flight_info(
            flight.FlightDescriptor.for_command(sql),
            options
        )
        reader = client.do_get(
            flight_info.endpoints[0].ticket, 
            options
        )
        
        df_output = reader.read_pandas()
        
        self._df = df_output
        
        return df_output
    
    
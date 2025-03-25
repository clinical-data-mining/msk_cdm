# How to connect PyCharm to a remote Jupyter kernel


### **Step 1: Start Jupyter on the Remote Server**
SSH into your remote machine and start Jupyter:

```bash
jupyter notebook --no-browser --port=8888 --ip=0.0.0.0
```

If you want to run it in the background:

```bash
nohup jupyter notebook --no-browser --port=8888 --ip=0.0.0.0 > jupyter.log 2>&1 &
```

You'll see an output like:

```
http://<remote-server-ip>:8888/?token=your_token_here
```

---

### **Step 2: Set Up an SSH Tunnel**
On your **local machine**, open a terminal and run:

```bash
ssh -L 8888:localhost:8888 your_username@your_remote_server
```

This forwards the remote Jupyter server to your local machine.

---

### **Step 3: Add Remote Jupyter Server in PyCharm**
1. **Open PyCharm**.
2. Go to **File** → **Settings** (or **Preferences** on macOS).
3. Navigate to **Project: [Your Project Name]** → **Python Interpreter**.
4. Click the gear icon ⚙ and select **Show All**.
5. Select your remote interpreter if it's already set up (or add it if not).
6. **Go to File → Settings → Jupyter**.
7. Click **Add Jupyter Server** → **New Server Configuration**.
8. Select **Configured Server**.
9. **Enter your Jupyter URL**, which should be:

   ```
   http://<server_name>:8888/tree?token=your_token_here

   ```

10. Click **Apply** and **OK**.

---

### **Bonus: Running Jupyter in a Conda/Virtual Environment**
If your Jupyter server runs inside a Conda or virtual environment, activate it before starting Jupyter:

```bash
# For Conda:
conda activate my_env
jupyter notebook --no-browser --port=8888 --ip=0.0.0.0

# For Virtualenv:
source my_env/bin/activate
jupyter notebook --no-browser --port=8888 --ip=0.0.0.0
```


![Maki Coin Bet Banner](bet.png)
# 🎲 Maki Coin Bet Automation Script

A simple, beginner-friendly Python script that **automates coin betting** on the **Maki Discord bot**.

No complicated setup. No programming knowledge required.

Just run it, switch to Discord, and let it do the work.

---

## ✨ What this script does

This script automatically performs the following loop:

1. Waits **10 seconds** so you can open Discord and place your cursor in chat box
2. Types `/coin`
3. Presses **Tab**
4. Chooses **Heads or Tails randomly**
5. Presses **Tab**
6. Types the bet amount (default: **200**)
7. Presses **Enter**
8. Waits **2 seconds**
9. Repeats 🔁

---

## 📈 Real Test Result (AFK)

Here’s a real example of performance:

- **Initial balance:** 4,174
- **Final balance:** 5,974
- **Total gain:** **+1,800**
- **Time:** 10 minutes
- **Bet amount used:** constant 200

⚠️ **Important:**

This result is **NOT guaranteed**. Your gains depend completely on **luck** and the **amount you bet**.

---

## ⚠️ Important Disclaimer

- This script **only automates typing** the commands you would normally type yourself.
- It does **NOT hack, exploit, or manipulate** the bot in any way.
- It does **NOT provide any unfair advantage**.
- Outcomes are **100% luck-based**.
- Always follow the **rules and Terms of Service of the Maki bot and Discord**.

---

## 🧰 Requirements

You only need:

- Python installed (type ‘python’ and install from microsoft store 3.10 or above versions)
- One library: `pyautogui`
- create a new folder (anywhere) named ‘bet’  and place the ‘bet.py’ file inside it
- navigate inside the created folder
- shift + right click in empty area inside folder
- select ‘open in terminal’
- type:

Install it with:

```bash
pip install pyautogui
```

---

## ▶️ How to use

1. Run the script
2. in terminal type ‘python -u bet.py’
3. press enter
4. You will see: **“Starting in 10 seconds…”**
5. Quickly switch to your **Discord window**
6. Make sure your cursor is active in the chat box
7. After 10 seconds, automation begins 🎯

---

## 🛑 Emergency Stop

At any time, you can stop the script by:

- Moving your mouse to the **top-left corner** of your screen
    
    *(PyAutoGUI failsafe)*
    
    **OR**
    
- Press **Ctrl + C** in your terminal

---

# ⚙️ Customization Guide (No Coding Experience Needed)

Below are the **exact lines** you can edit in the script to change behavior. (use notepad or any text editor to edit)

---

## ⏱️ Change the starting delay (default 10 seconds)

```python
time.sleep(10)
```

👉 Want more time to switch windows?

Change `10` to `15` or `20`

---

## 🔁 Change delay between each bet (default 2 seconds)

At the very bottom:

```python
time.sleep(2)
```

👉 If Maki gives you a **cooldown warning**, increase this to:

```python
time.sleep(3)# or
time.sleep(5)
```

---

## 💰 Change the constant bet amount (default 200)

Find this line:

```python
pyautogui.write('200')
```

👉 Replace `'200'` with your desired amount:

```python
pyautogui.write('500')
```

---

## 🎯 Use a RANDOM bet range instead of fixed amount

Replace this line:

```python
pyautogui.write('200')
```

With this block:

```python
import random
amount =str(random.randint(100,500))
pyautogui.write(amount)
```

👉 This will bet **randomly between 100 and 500 each time**

You can change the range here:

```python
random.randint(100,500)
```

---

## 🎲 Heads or Tails is already random

This part of the script:

```python
choice = random.choice(['heads','tails'])
```

Already ensures each bet is **randomly selected**.

---

# 💡 Tips for Best Results

- Start with a **safe amount**
- Use **consistent betting** or small ranges
- Increase delay if you see **cooldowns**
- Let it run for **short sessions first** and observe results

---

# 🎮 Who is this for?

This script is perfect for:

- People who want to **AFK farm coins**
- Users who don’t want to type commands repeatedly
- Anyone who wants a **simple, no-coding automation tool**

---

# ❤️ Final Words

This tool is made for **convenience and fun**.

It **does not guarantee profit**, does not exploit anything, and simply automates repetitive input.

Your results will always depend on:

🎲 **Luck**

💰 **Your bet amount**

⏳ **How long you run it**

---

Enjoy and use responsibly ✨

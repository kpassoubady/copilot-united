# FAQs

## If I get the below error how can I look at the logs

```text
Sorry, your request failed. Please try again. Request id: 676b8c54-80e7-430a-bca5-76bb88b9a70c
Reason: Error on conversation request. Check the log for more details.
```

You can find the GitHub Copilot logs within the Output panel of Visual Studio Code.

Here’s how to access them:

1. Open the Command Palette: Press **Ctrl+Shift+P** (Windows/Linux) or **Cmd+Shift+P** (Mac).
2. Show Output Channels: Type **Output: Show Output Channels** and press Enter. This will open the Output panel at the bottom of your editor.
3. Select the Copilot Channel: In the top-right corner of the Output panel, you'll see a dropdown menu. Click it and select one of the following channels:
    - GitHub Copilot
    - GitHub Copilot Chat

This will display the detailed logs for the respective Copilot service, which is useful for troubleshooting any issues.

## Additional Troubleshooting

For more in-depth diagnostics, you can also:

- **Collect Diagnostics**: Open the Command Palette (**Ctrl+Shift+P** or **Cmd+Shift+P**), type **GitHub Copilot: Collect Diagnostics**, and press Enter. This will open a new tab with detailed diagnostic information.
- **Open Extension Logs Folder**: In the Command Palette, run **Developer: Open Extension Logs Folder**. This will open your system's file explorer to the directory where VS Code stores logs for all extensions, including Copilot.

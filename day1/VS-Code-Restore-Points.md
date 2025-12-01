# Best Methods to Create Restore Checkpoints in VS Code

## 1. Best for Automatic Checkpoints: Use the Timeline View (Local History)

VS Code automatically saves a history of your changes every time you save a file. This is the quickest and easiest way to create checkpoints without any manual effort.

**Save Your File:** Before you ask Copilot for a significant change, simply save the file (Ctrl+S or Cmd+S). This creates a checkpoint in the local history.

**Open the Timeline:** In the Explorer panel on the left, you'll see a "Timeline" view at the bottom. If you don't see it, you can open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and type "Timeline: Show Timeline".

**Restore a Checkpoint:** The timeline shows a list of all the times you saved the file. You can click on any previous save to see a "diff" view of the changes and click the Restore button to revert to that version.

## 2. Best for Major Checkpoints: Use Git Commits

For more significant, deliberate checkpoints (e.g., before refactoring a whole class with Copilot), using Git is the standard and most robust method.

**Stage and Commit:** Before you start, make sure your current work is saved and committed to Git. Go to the Source Control view (the branching icon on the left sidebar).

- Stage your changes by clicking the '+' icon.
- Write a commit message like "Checkpoint before Copilot refactoring."
- Click the checkmark to commit.

**Use Copilot:** Now, feel free to accept any and all suggestions from Copilot.

**Revert if Needed:** If you're not happy with the changes, you can easily discard everything and go back to your last commit. In the Source Control view, right-click on the changed file and select "Discard Changes".

## 3. Best for Immediate Reversal: Use Undo

Don't forget the simplest method! If you accept a suggestion from Copilot and immediately realize you don't want it, just use the undo command.

- **Windows/Linux:** Ctrl+Z
- **Mac:** Cmd+Z

This will instantly revert the code that Copilot just added.

## Recommended Workflow

- **For small changes:** Rely on Undo (Ctrl+Z).
- **For medium changes or after a few minutes of work:** Save your file and use the Timeline view to go back.
- **For major changes or before starting a new feature:** Use Git commits as your solid, named checkpoints.

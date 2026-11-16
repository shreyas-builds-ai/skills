# Prompter

**Rough idea in, ready-to-paste prompt out.** Write what you want in English, Hindi or Hinglish. Prompter turns it into a clear prompt for ChatGPT, Claude, Gemini, image generators or coding assistants, and tells you in one line per change *why* it works, so you get better at prompting yourself.

No secret codes, no "GODMODE". Just clear words: what to do, for whom, with what input, in what shape.

From [Shreyas Builds AI](https://www.instagram.com/shreyas.builds.ai) · *Hype nahi, hakikat.*

---

## Two ways to use it

| You use | Use this | Cost |
|---|---|---|
| **Claude** (claude.ai, free or paid) or Claude Code | The **Prompter skill** (`prompter/` folder) | Free |
| **ChatGPT** (any plan, including free) | **[chatgpt-codes.md](chatgpt-codes.md)**: paste one block into Custom Instructions | Free |

## Install the skill on claude.ai (free plan works)

1. Download **`prompter.zip`** from the [Releases](../../releases) page of this repo.
   (Don't use GitHub's green "Code → Download ZIP" button: that ZIP has the wrong folder name and the upload fails.)
2. On claude.ai, open **Settings → Capabilities** and turn on **Code execution and file creation** (in newer layouts it's called **Create and edit files**). Skills need it.
3. Go to **Customize → Skills**, click **+**, choose **Create skill → Upload a skill**, and pick `prompter.zip`.
4. Make sure Prompter is switched on. Done.

## Install in Claude Code

Copy the `prompter/` folder into `~/.claude/skills/` (all projects) or `.claude/skills/` inside one project.

## How to use

Just ask, or start with a command:

| Command | What it does | Example |
|---|---|---|
| `/prompt` | Builds a new prompt | `/prompt kal data analyst ka interview hai, mock interview chahiye` |
| `/fix` | Improves a prompt you already have | `/fix write a good linkedin post about my new job` |
| `/img` | Builds an image prompt | `/img chai on a window sill at sunset, Instagram post` |
| `/codes` | Writes your own shortcodes for Custom Instructions | `/codes main roz emails aur meeting notes ke liye use karta hoon` |

You get:
1. One prompt in a copy-ready block.
2. **Kyun yeh kaam karega:** 2–4 one-line reasons.
3. Sometimes one tip to make it even better.

It asks at most two questions, and only when it really can't guess.

## What's inside

```
prompter/
  SKILL.md               the skill
  references/
    image.md             image prompt structure, light and camera words, what doesn't work
    examples.md          before/after examples (emails, interviews, concepts, LinkedIn, shortcodes)
chatgpt-codes.md         ChatGPT Custom Instructions version (909 characters)
```

## Licence

MIT, see [LICENSE](LICENSE).

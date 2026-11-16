<p align="center">
  <img src="assets/banner.png" alt="@shreyas.builds.ai · Skills I build, free to install" width="100%">
</p>

# skills

Free AI skills from [@shreyas.builds.ai](https://www.instagram.com/shreyas.builds.ai). *Hype nahi, hakikat.*

I'm Shreyas, a senior AI/ML engineer. On Instagram I check AI claims and show what actually works, for students and working professionals in India. When a reel or carousel ends with "comment KEYWORD" and promises a tool, this is where the tool lives.

## What is a skill?

A skill is a folder with a `SKILL.md` file in it: plain-English instructions, plus reference files when needed. You install it once, and your AI loads it when your request matches. After that you just ask.

Nothing is hidden. Open any `SKILL.md` and you can read every word the AI will read.

## Skills

| Skill | What it does | Works with |
|---|---|---|
| [**Prompter**](prompter/) | Write a rough idea in English, Hindi or Hinglish and get a ready-to-paste prompt back, with one line on why each change works. Commands: `/prompt`, `/fix`, `/img`, `/codes` | Claude (claude.ai and Claude Code), plus a ChatGPT version for Custom Instructions |

More are coming. Follow [@shreyas.builds.ai](https://www.instagram.com/shreyas.builds.ai) to hear when a new one drops.

## Install

### claude.ai: website or app (the free plan works)

1. **Download** the skill: [**prompter.zip**](https://github.com/shreyas-builds-ai/skills/raw/main/prompter/prompter.zip) (one click).
2. On claude.ai, open **Settings → Capabilities** and turn on **Create and edit files** (older layouts: *Code execution and file creation*).
3. Open **Customize → Skills**, tap **+ → Upload a skill**, and choose the file you downloaded. Done.

Use the download link above, not GitHub's green **Code → Download ZIP** button: that ZIP has the wrong folder name and the upload fails.

### ChatGPT (any plan)

ChatGPT doesn't load skills. Open [chatgpt-codes.md](prompter/chatgpt-codes.md), copy the block, and paste it into **Settings → Personalization → Custom Instructions**.

### Claude Code

Paste this into Claude Code:

```
Install the prompter skill from https://github.com/shreyas-builds-ai/skills: copy the folder prompter/prompter/ into ~/.claude/skills/prompter/
```

Or with one command (needs [Node.js](https://nodejs.org)):

```bash
npx skills add shreyas-builds-ai/skills --skill prompter
```

Or by hand: copy `prompter/prompter/` into `~/.claude/skills/` (every project) or `.claude/skills/` (one project).

## House rules

Every skill in this repo:

1. **Is plain text you can read.** No hidden prompts, no tracking, no API keys.
2. **Promises no magic.** No "GODMODE", no secret codes, no "unlock". A skill works because its instructions are clear, and that's all.
3. **Is tested before it goes up.** I run it on real tasks first. If it doesn't hold up, it doesn't ship.
4. **Understands how you talk.** Ask in English, Hindi or Hinglish.
5. **Is free.** Each skill carries its own licence.

## Repo layout

```
skills/
├── README.md                you are here
├── assets/banner.png
├── tools/make-zips.py       builds every <name>/<name>.zip
└── prompter/
    ├── README.md            install and usage guide
    ├── prompter.zip         one-click download for claude.ai
    ├── LICENSE
    ├── chatgpt-codes.md     ChatGPT version
    └── prompter/            the skill folder you install
        ├── SKILL.md
        └── references/
```

Every new skill follows the same shape: `<name>/README.md` for people, `<name>/<name>/SKILL.md` for the AI, and `<name>/<name>.zip` for claude.ai. After changing a skill, run `python tools/make-zips.py` and commit the new ZIP with the change.

## Found a problem?

Open an [issue](../../issues) with what you asked, what you expected and what you got. Or DM me on Instagram.

## Licence

Each skill has its own `LICENSE` file. Prompter is MIT.

---

<p align="center">
  Made by <a href="https://www.instagram.com/shreyas.builds.ai"><b>@shreyas.builds.ai</b></a> · Hype नहीं, हकीकत
</p>

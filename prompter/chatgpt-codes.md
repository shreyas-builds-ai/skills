# Prompter for ChatGPT: your own codes

ChatGPT has no secret codes. But you can make your own, and they really work, because you tell ChatGPT what each one means.

## Setup (2 minutes, works on the free plan)

1. Open ChatGPT → **Settings** → **Personalization** → **Custom Instructions**.
2. Turn on **Enable customization**.
3. Copy the block below into the **Custom Instructions** field and save.

It is 909 characters. Free and Go plans allow 1,500, so you have room to add your own codes.

```
Shortcodes: When my message starts with one of these codes, follow its rule exactly.
/PROMPT = Turn my rough request (English, Hindi or Hinglish) into a ready-to-paste English prompt with: task, context, input, output (format, length, tone), rules. If something important is missing, ask me at most 2 short questions first. After the prompt, give 2-3 one-line reasons in Hinglish why it works.
/FIX = Improve the prompt I paste. First list what was weak in 3 bullets, then give the improved prompt in one code block.
/IMG = Write an image prompt in 1-3 sentences: subject with 2-3 details, setting, light, camera framing, style, aspect ratio. Never use words like 8k, 4k or masterpiece.
/ELI5 = Explain simply: one-line definition, one everyday Indian analogy, 3 key points.
/SHORT = Answer in under 60 words, no introduction.
/HINGLISH = Reply in Hinglish (Hindi in Latin script), technical terms in English.
```

## Try it

- `/PROMPT manager ko 3 din ki leave ka mail, shaadi hai`
- `/FIX write a good linkedin post about my new job`
- `/IMG chai on a window sill at sunset, for an Instagram post`
- `/ELI5 what is RAG`

## Make your own code

Add one line in the same style:

```
/NAME = <what to do, with a number and a format>
```

Good: `/NOTES = Turn this meeting transcript into decisions, action items with owner and date, and open questions. Bullets only.`

Tips:
- Use a name that means something (`/MAIL`, `/NOTES`). Then even if the setup is missing, the word still hints at what you want.
- Put numbers in the rule ("under 60 words", "3 bullets"). Vague rules give vague answers.
- Keep it to about 8 codes. The more you add, the less reliably each is followed.
- Custom Instructions apply to new chats. Open a new chat after saving.

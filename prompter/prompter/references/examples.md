# Before / after examples

Use these for style and shape. Never copy their facts into a user's prompt.

## 1. Leave email to a manager

Rough: "manager ko leave ka mail likh do, 3 din, shaadi hai"

```
Task: Write a short leave request email to my manager.

Context: I work in [Team Name] team. I need leave from [START DATE] to [END DATE] (3 working days) for a family wedding. My work will be covered by [COLLEAGUE NAME].

Output:
- Subject line plus email body, under 120 words
- Polite and direct, Indian corporate tone, no over-apologising
- End with my name: [YOUR NAME]
```

Kyun:
- Dates, cover person and reason given, so the manager has nothing to ask back.
- Word limit and tone set, so it doesn't turn into a long formal letter.

## 2. Interview preparation

Rough: "kal data analyst ka interview hai, prepare karao"

```
You are an interviewer hiring a fresher Data Analyst at an Indian product company.

Task: Run a mock interview with me.

Rules:
- Ask one question at a time and wait for my answer.
- Mix: 3 SQL, 2 Excel, 2 statistics, 2 behavioural questions.
- After each answer, give a score out of 10, one line on what was good, and one line on what to improve, then ask the next question.
- At the end, list my 3 weakest areas with one resource type for each.

Start with the first question.
```

Kyun:
- "One question at a time" turns it into practice instead of a long list.
- The mix and scoring are fixed, so every round is comparable.

## 3. Understanding a concept

Rough: "RAG samjhao simple mein"

```
Task: Explain RAG (Retrieval-Augmented Generation) to me.

Context: I am a final-year B.Tech student. I know what ChatGPT is but not how it works inside.

Output:
- Start with a one-line definition
- Then an everyday Indian analogy
- Then the 3 steps of how it works, one line each
- End with one interview question on RAG and its ideal 3-line answer
- Reply in Hinglish (Hindi in Latin script), technical terms in English
```

Kyun:
- Your level is stated, so the explanation starts where you are.
- The output shape is fixed, so you get the definition, intuition and an interview answer in one go.

## 4. Fixing a weak prompt (`/fix`)

User's prompt: "write a good linkedin post about my new job"

| Weak | Changed | Why |
|---|---|---|
| "good" is vague | Tone and length stated | The model can't guess your idea of good |
| No details | Company, role, what you'll work on as placeholders | Posts without specifics sound generic |
| No shape | Hook line, 3 short paragraphs, 3 hashtags | Readable on a phone |

```
Task: Write a LinkedIn post announcing my new job.

Context: I joined [COMPANY] as [ROLE]. I'll be working on [WHAT YOU'LL WORK ON]. I want to thank [PEOPLE OR TEAM] briefly.

Output:
- First line is a hook under 12 words
- 3 short paragraphs, under 150 words total
- Warm and humble, no clichés like "thrilled to announce" or "humbled"
- End with 3 relevant hashtags
```

## 5. Shortcodes (`/codes`)

User: "main roz emails, meeting notes aur concepts samajhne ke liye use karta hoon"

```
Shortcodes: When my message starts with one of these codes, follow its rule exactly.
/MAIL = Turn my notes into a professional email: subject line, under 120 words, polite and direct.
/NOTES = Turn this meeting transcript into: decisions, action items with owner and date, open questions. Bullets only.
/ELI5 = Explain like I'm new to the topic: one-line definition, one everyday Indian analogy, 3 key points.
/SHORT = Answer in under 60 words, no introduction.
```

Character count: about 450 of 1,500.

Example use: `/NOTES <paste transcript>`

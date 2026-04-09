# Dayou Content Pipeline — RUNBOOK

> For non-technical team members: masters, content reviewers, and marketing operators.

## Your Role

You don't need to write code. Your job is:
1. **Submit content ideas** (weekly, via GitHub Issue)
2. **Review generated scripts** (approve or request changes)
3. **Track performance** (weekly, via GitHub Issue)

---

## Getting Started (One-Time Setup)

### 1. Create a GitHub Account
- Go to https://github.com/join
- Sign up with your email
- Ask the project owner to add you as a collaborator on `AlyciaBHZ/dayou-content`

### 2. Clone the Repository (Optional)
If you want to see files locally:
```bash
git clone https://github.com/AlyciaBHZ/dayou-content.git
cd dayou-content
```

But you can also just use the GitHub website to browse files and create issues.

---

## Weekly Workflow

### Monday: Submit Content Ideas

1. Go to https://github.com/AlyciaBHZ/dayou-content/issues/new/choose
2. Select "Content Idea Submission"
3. Fill in 2-3 concepts for the week. Examples:
   - "Explain 'Water overcomes Fire' in the context of workplace conflict"
   - "Yi Jing hexagram 2 (Kun): the power of receptivity"
   - "Five Elements in daily decision making"
4. Submit the issue

### Tuesday-Wednesday: Review Generated Scripts

1. The pipeline generates 7 scripts based on your ideas + the corpus
2. You'll find them in `workspace/scripts/YYYY-WXX/scripts/`
3. On GitHub, navigate to that folder and read each `.md` file
4. Comment on the GitHub Issue if anything needs changes:
   - "Script 03 feels too abstract, add a concrete example"
   - "The CTA should mention 'birth element' not 'destiny'"
   - "This one is great, approve"

### Thursday: Scripts Finalized & Videos Generated

After your approval, the pipeline generates HeyGen avatar videos.

### Friday-Sunday: Content Published

Videos are published to TikTok daily via the automated pipeline.

---

## How to Submit a Content Idea (Step by Step)

### On GitHub (Recommended)

1. Open https://github.com/AlyciaBHZ/dayou-content/issues
2. Click "New Issue"
3. Choose "Content Idea Submission"
4. Fill in the template:
   - **Source text**: Which classic? (Yi Jing, Dao De Jing, etc.)
   - **Concept**: What's the core idea? (1-2 sentences)
   - **Angle**: How does this apply to modern life?
   - **Target emotion**: What should the viewer feel?
5. Submit

### Via WeChat (Fallback)

Send the project owner a voice memo or text with:
- Which classic text
- The concept in 1-2 sentences
- How it applies to modern life

The owner will create the GitHub Issue on your behalf.

---

## How to Review Scripts

Each script follows this format:

```
## HOOK (0-3 seconds)
One provocative sentence to grab attention

## BODY (3-45 seconds)
The main teaching, 2-3 key points

## CTA (45-60 seconds)
Soft invitation to follow or try a reading

## CAPTION
Text that appears below the video on TikTok

## VISUAL_DIRECTION
Notes for video production
```

### What to check:
- Is the HOOK attention-grabbing? Would you stop scrolling?
- Is the BODY accurate to the original teaching?
- Does the cultural translation feel natural in English?
- Is anything misleading or could be misunderstood by Western audiences?

### How to give feedback:
Comment directly on the GitHub Issue with specific notes:
- "Script 02: The body is too long, cut point #3"
- "Script 05: Great hook, but the Five Elements explanation needs the water/fire analogy"

---

## Cultural Translation Reference

When reviewing scripts, ensure these rules are followed:

| Original Chinese | English Translation | Why |
|-------------------|--------------------|----|
| 紫微斗数 | "Chinese star destiny chart" | Nobody knows the Chinese term |
| 八字 | "birth element blueprint" / "Four Pillars" | Recognized in English spiritual circles |
| 算命 | "personality mapping" / "destiny analysis" | Avoids "fortune telling" stigma |
| 风水 | "spatial energy" / "environmental harmony" | Known but loaded with cliches |
| 玄学 | "Chinese metaphysics" / "Eastern wisdom" | Professional, neutral framing |

Full reference: see `CULTURAL_TRANSLATION.md` in this repo.

---

## Weekly Progress Report

Every Sunday, create a GitHub Issue with the "Weekly Report" template:

1. How many videos were published this week?
2. Top-performing video (views, likes, comments)
3. Any interesting comments or DMs from viewers?
4. Content ideas for next week
5. Any problems or blockers?

---

## FAQ

**Q: I made a mistake in an issue, can I fix it?**
A: Yes, you can edit any issue you created by clicking the "..." menu.

**Q: How do I see the generated videos?**
A: Videos are stored in `workspace/videos/`. You can also see them on the TikTok account directly.

**Q: Can I suggest changes to the avatar's style or voice?**
A: Yes! Create a regular issue with your suggestion. The owner will adjust the HeyGen config.

**Q: I have urgent feedback, what do I do?**
A: WeChat the project owner directly for anything urgent. GitHub Issues are for async workflow.

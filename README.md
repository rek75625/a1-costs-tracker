# a1-costs-tracker

# Assignment 1: Comparing LLM Providers

For this assignment, I wrote a quick Python script that sends the exact same prompt to two different AI providers—**Groq** (`openai/gpt-oss-120b`) and **Google Gemini** (`gemini-2.5-flash`). It prints out the responses from both models alongside their input/output token counts and what each call would cost based on standard API pricing.

## What You'll Need

- Python 3.10 or newer
- [uv](https://astral.sh) installed to manage the environment and dependencies

## Getting Started

1. Clone the repo and jump into the project folder:
   ```bash
   git clone <your-repo-url>
   cd assignment-1
   ```
2. Add a `.env` file in the main directory and drop in your API keys:
   ```env
   GROQ_API_KEY=GROQ_API_KEY
   ```

## Running the Script

Once your `.env` file is ready, just run:

```bash
uv run main.py
```

## Example Output

```text
<Paste your terminal output from `uv run main.py` here>
```

# ==================================================================================

=== Provider 1: Groq (openai/gpt-oss-120b) ===
Reply:
**Qur’an and Ḥadīth (sometimes written “Quran o Hadith”) are the two primary sources of Islamic belief, law, and practice.**  
Both are essential for Muslims, but they serve different roles and have different origins.

---

## 1. The Qur’an (Arabic: القرآن)

| Aspect             | Description                                                                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **What it is**     | The Qur’an is considered the _direct_ word of God (Allah) revealed in Arabic to the Prophet Muhammad (peace be upon him) over a period of about 23 years (610–632 CE).               |
| **Form**           | A single, cohesive text of 114 chapters (surahs), each made up of verses (ayahs). It is recited, memorized, and written in a highly stylized Arabic prose.                           |
| **Authority**      | The Qur’an holds the highest authority in Islam. Every Muslim is required to believe that it is the final, unchanged revelation from God, preserved exactly as it was revealed.      |
| **Content**        | It covers theology (the oneness of God, the after‑life), morality, law, guidance for personal conduct, social relations, worship, stories of earlier prophets, and more.             |
| **How it is used** | • Recited in daily prayers and on many other occasions.<br>• Studied and interpreted (tafsīr) to understand its meanings.<br>• Forms the basis for Islamic law (sharīʿa) and ethics. |

---

## 2. The Ḥadīth (Arabic: الحديث)

| Aspect                | Description                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it is**        | Ḥadīth are reports of the _sayings, actions, approvals, or characteristics_ of the Prophet Muhammad (peace be upon him). They are not the Qur’an itself, but they convey how the Prophet understood and applied the Qur’anic message.                                                                                                                                         |
| **Components**        | A typical Ḥadīth consists of two parts: <br>• **Isnād** – the chain of narrators who transmitted the report.<br>• **Matn** – the actual text of the report.                                                                                                                                                                                                                   |
| **Authority**         | While the Qur’an is the primary source, the Ḥadīth are the secondary source that explains, details, and contextualizes Qur’anic teachings. They are essential for deriving Islamic law (fiqh) and for modeling the Prophet’s conduct (the “Sunnah”).                                                                                                                          |
| **Classification**    | Scholars have graded Ḥadīth according to the reliability of their chains and content: <br>• **Ṣaḥīḥ** (authentic) –strongest, most reliable.<br>• **Ḥasan** (good) – reliable but with minor weaknesses.<br>• **Ḍa‘īf** (weak) – not reliable enough for legal rulings.                                                                                                       |
| **Major Collections** | The most widely accepted Sunni collections (considered the most reliable) are: <br>• **Ṣaḥīḥ al‑Bukhari** (by Muhammad al‑Bukhari) <br>• **Ṣaḥīḥ Muslim** (by Muslim ibn al‑Hajjaj) <br>Other important compilations include those of Abu Dawūd, al‑Tirmidhī, al‑Nāsāʾī, and Ibn Māja. <br>In Shiʿa Islam, the primary collections are **Al‑Kāfī**, **Manāqib al‑Āyāt**, etc. |
| **How it is used**    | • To explain verses of the Qur’an that are brief or ambiguous.<br>• To provide details of worship (e.g., how to pray, fast, perform Hajj).<br>• To derive legal rulings on matters not explicitly covered in the Qur’an.<br>• To serve as a moral and spiritual model for Muslims.                                                                                            |

---

## 3. Relationship Between Qur’an and Ḥadīth

1. **Complementary, not contradictory** – Ḥadīth must be in harmony with the Qur’an. If a reported tradition appears to conflict with the Qur’an, scholars investigate its authenticity; often it turns out to be weak or misinterpreted.
2. **Qur’an is the _source_; Ḥadīth are the _exposition_** – The Qur’an says _“obey Allah and obey the Messenger”_ (Qur’an 4:59). The Ḥadīth show what “obeying the Messenger” looks like in practice.
3. **Legal methodology (Usul al‑Fiqh)** – Islamic jurists (fuqaha) use a hierarchy: first the Qur’an, then authentic Ḥadīth, then consensus (ijmā‘), then analogical reasoning (qiyās).

---

## 4. Why Both Are Important for Muslims

- **Spiritual Guidance:** The Qur’an provides the divine message; the Ḥadīth provide the Prophet’s example, making the divine guidance tangible in daily life.
- **Legal Framework:** Many detailed rulings (e.g., specifics of prayer, inheritance, commercial transactions) come from the Ḥadīth, because the Qur’an often states principles in broader terms.
- **Moral Modeling:** Muslims view the Prophet as the “best exemplar” (al‑uswā bil‑ḥusna). Following his reported actions and sayings helps believers embody Qur’anic ethics.

---

## 5. Quick Summary for a Beginner

- **Qur’an** = _the holy book_, believed to be the exact words of God revealed to Muhammad.
- **Ḥadīth** = _the recorded sayings and actions_ of Muhammad, preserving how he lived out the Qur’an.
- Both together form the foundation of **Islamic theology, law, and moral practice**.

---

### A Simple Analogy

Think of the Qur’an as a **blueprint** for a house. It tells you the overall design, the materials you must use, and the purpose of each room. The Ḥadīth are the **construction manual** written by the master builder (the Prophet) that shows step‑by‑step how to actually build the house according to the blueprint. Without the manual, you might understand the design, but you would lack the practical details needed to bring it to life.

---

**If you’d like to explore further**, you might start with:

1. Reading a reputable translation of the Qur’an (e.g., Sahih International, Muhammad Marmaduke Pickthall, or the Quran.com website).
2. Looking at an introductory collection of authentic Ḥadīth, such as _Riyāḍ al‑Sālihīn_ (a selection of Bukhari & Muslim) or the _Forty Hadith of Imam Nawawi_—both are widely used for beginners.

Feel free to ask if you’d like recommendations for specific topics, books, or explanations of particular verses or traditions!

Input Tokens: 79
Output Tokens: 1560
Cost: $0.000948 (Free tier - theoretical paid cost)

# -------------------------------------------------------------------------------------------------

                                   Response By google Gemini

# -------------------------------------------------------------------------------------------------

Reply:
The phrase **"Quran o Hadith"** (often written in Urdu/Persian as _Quran-o-Hadith_, where the "o" means **"and"**) refers to the **Quran and the Hadith**.

Together, they form the **two primary, foundational sources of guidance, law, and theology in Islam**. A Muslim's faith, daily practice, and moral code are derived directly from these two sources.

Here is a breakdown of what each represents and how they work together:

---

### 1. The Quran (The Word of God)

- **What it is:** The Holy Book of Islam, which Muslims believe is the literal, verbatim word of Allah (God).
- **How it was revealed:** It was revealed to the Prophet Muhammad (peace be upon him) over a period of approximately 23 years through the Angel Gabriel (Jibril).
- **Role:** It is the highest and most sacred authority in Islam. It outlines the fundamental beliefs (such as the oneness of God, the afterlife, and prophethood), moral principles, basic legal frameworks, and stories of past nations and prophets.
- **Preservation:** Muslims believe the Quran is preserved in its original Arabic text without alteration.

---

### 2. The Hadith (The Prophetic Traditions)

- **What it is:** The recorded collection of the **sayings, actions, habits, and tacit approvals** (things he saw and did not forbid) of the Prophet Muhammad (peace be upon him).
- **Role:** While the Quran provides the direct divine message, the Hadith records how the Prophet implemented that message in daily life. This lived example is known as the **Sunnah**.
- **Authentication:** Unlike the Quran, which was memorized and recorded in full during and immediately after the Prophet’s lifetime, Hadiths were compiled by scholars (such as Imam Bukhari and Imam Muslim) who created a rigorous science of authentication to verify which reports were authentic (_Sahih_), acceptable (_Hasan_), or weak (_Da'if_).

---

### How They Work Together

The Quran and Hadith are complementary and inseparable in practice:

1. **Broad Principles vs. Practical Details:**
   - The Quran often gives broad commands, while the Hadith provides the specific instructions.
   - _Example:_ The Quran commands Muslims to **pray (Salah)** and pay **alms (Zakat)**, but it does not specify the exact movements of prayer, the number of units (_rak'ahs_), or the specific percentages to give for charity. The Hadith provides these exact details through the Prophet's words: _"Pray as you have seen me pray."_

2. **Explanation and Context:**
   - The Hadith explains the historical context (_Asbab al-Nuzul_) behind why certain verses of the Quran were revealed, helping scholars interpret them accurately.

3. **Moral Example:**
   - When the Prophet’s wife, Aisha, was asked about his character, she famously replied: _"His character was the Quran."_ This means the Hadith shows the Quran in human action.

---

### Summary

When someone uses the phrase **"Quran o Hadith,"** they are referring to the complete bedrock of Islam: **the Quran provides the divine constitution, andthe Hadith provides the practical guide on how to live by it.**

Input Tokens: 9
Output Tokens: 707
Cost: $0.001770 (Free tier - theoretical paid cost)

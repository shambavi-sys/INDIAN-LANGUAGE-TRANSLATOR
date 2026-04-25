# Indian Language Translator – QA Testing Portfolio

> **Tested by:** Sambavi B | QA Engineer | sambavib40@gmail.com  
> **Testing Period:** February 2025 – June 2025  
> **Project Type:** Academic Final Year Project + QA Portfolio

---

## About This Repository

This repository contains the source code **and complete QA documentation** for an Indian Language Translator application built using Python (Tkinter). The application supports translation between English and 6 Indian languages: **Tamil, Hindi, Telugu, Kannada, Malayalam, and Bengali**.

As the QA tester for this project, I designed and executed a full manual testing cycle — covering functional, compatibility, performance, API, regression, smoke, and sanity testing.

---

## QA Documents in This Repo

| File | Description |
|------|-------------|
| `Test_Cases_Translator.xlsx` | 40 test cases with steps, expected vs actual results, and pass/fail status |
| `Bug_Report_Translator.xlsx` | 5 bug reports with severity, priority, reproduction steps, and resolution |
| `FINAL REPORT (2).pdf` | Complete project report including testing methodology |
| `PIP 4004.pptx` | Project presentation |

---

## Testing Summary

| Metric | Value |
|--------|-------|
| Total Test Cases | 40 |
| Pass | 33 |
| Fail | 5 |
| Blocked | 2 |
| Pass Rate | 82.5% |
| Bugs Reported | 5 |
| Bugs Fixed | 3 |
| Languages Tested | 6 |

---

## Testing Types Performed

- **Functional Testing** – Verified core translation features for all 6 languages
- **Compatibility Testing** – Tested on Windows 10 and Windows 11
- **Performance Testing** – Measured response time and load handling
- **API Testing** – Validated REST endpoints using Postman
- **Regression Testing** – Re-verified fixed bugs after each patch
- **Smoke Testing** – Quick sanity checks after each build deployment
- **Negative Testing** – Empty input, special characters, unsupported language codes

---

## Tools Used

| Tool | Purpose |
|------|---------|
| JIRA | Bug tracking and defect management |
| TestRail | Test case management |
| Postman | API testing (REST endpoint validation) |
| Excel | Test documentation and reporting |
| Python 3.11 | Application language |

---

## Key Bugs Found

| Bug ID | Title | Severity | Status |
|--------|-------|----------|--------|
| BUG_001 | Same-language selection produces no warning | Medium | Fixed |
| BUG_002 | API returns HTTP 500 for unsupported language code | High | Fixed |
| BUG_003 | App becomes unresponsive after 8 rapid requests | High | Open |
| BUG_004 | Telugu script shows glyph misalignment | Medium | Open |
| BUG_005 | Long paragraph (500+ chars) gets truncated | High | Fixed |

---

## About Me

I am a B.Tech Information Science graduate (Presidency University, 2025) with strong skills in manual testing, API testing, and defect management. I am actively seeking entry-level QA / Software Tester roles in Chennai.

- **Email:** sambavib40@gmail.com
- **LinkedIn:** linkedin.com/in/sambavib
- **Skills:** Manual Testing · JIRA · Postman · TestRail · STLC · SDLC · Black Box Testing

---

*This repository serves as part of my QA portfolio to demonstrate real-world testing skills to potential employers.*

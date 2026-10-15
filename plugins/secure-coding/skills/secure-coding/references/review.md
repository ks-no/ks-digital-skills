# Review of application code

Load this file when the user asks for a review or an audit of code, a diff, a pull
request or a repository.

## Scope

- For a branch or a pull request, review the changed files. Compare with the merge
  base of the default branch. Also read the code that the change calls or that calls
  the change, when you need it to judge a finding.
- For an audit, start with the entry points: HTTP handlers, message consumers,
  scheduled jobs and command-line entry points.
- Say at the start what you reviewed and what you did not review.

## Method

1. **Trust boundaries.** Find where data comes in: requests, headers, files,
   messages, other services, model output.
2. **Source to sink.** Follow each input to the places where it is used: queries,
   commands, file paths, templates, headers, deserializers, logs, outgoing requests.
3. **Access.** For each handler, find the authentication and the check for the
   object or the tenant.
4. **Configuration.** Read only the settings that the change touches.

## When to report a finding

Report a finding only when you can describe a concrete path from an attacker to an
impact, and you are at least 80% sure that it works. Name the attacker: anyone on
the internet, a logged-in user, a user in another tenant, or an administrator.
Describe the path in words. Do not write a working payload.

| Severity | Typical example |
| --- | --- |
| Critical | Anyone runs code on the server, or reads or changes data of all tenants without login. |
| High | A logged-in user reads or changes data of another user or tenant, runs code on the server, or sends as another person. |
| Medium | Personal data or tokens in logs, an open redirect, an error that shows internal details. |
| Low | Hardening without a known attack path. |

Severity depends on the attacker and the impact, not on the type of bug. A missing
check that a framework default already covers is not high.

## These are not findings

- A query part that comes from a fixed set, for example a `switch` on an enum or a
  lookup in a fixed map, and is then joined into the SQL text.
- Bound parameters: `$1`, `?`, `:name`, `@Name`, and `FromSql` or `ExecuteSql` in
  EF Core 7 or later.
- A hash such as SHA-256 that makes an ETag, a cache key or a checksum. A fast hash
  is wrong for passwords and for signatures, not for these uses.
- An access check in a component that you cannot see, for example
  `@PreAuthorize("@access.canRead(authentication, #id)")`. Do not report it. If the
  answer depends on it, add a `Check:` line that the component does what its name
  says.
- A missing rate limit, audit log, security header or input length limit, when the
  change does not touch that area.

When the code has no real problem, say so in one sentence. You can add up to three
low notes after it.

## Finding format

For each finding, give:

- **Title** and **severity** (critical, high, medium or low)
- **Location**: `file:line`
- **Attacker and path**: who can do it, and how, in two or three sentences
- **Impact**: what the attacker gets
- **Fix**: the smallest change that removes the problem, as code. Keep the routes,
  status codes, field names and behaviour. Use only names that exist.
- **ID**: the OWASP risk and, if useful, the CWE

Start the report with one to three lines that give the result. Order the findings
from critical to low. If you find nothing, say "No findings", and list what you
checked. That is a valid result.

If your tool can start a separate agent with a fresh context, give it each critical
or high finding, and let it confirm or reject the finding. If not, check each one
again yourself against the list "These are not findings".

## OWASP IDs

Use the ID and the name. Do not copy text from OWASP.

| List | IDs |
| --- | --- |
| OWASP Top 10:2025 | A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions |
| OWASP API Security Top 10:2023 | API1 Broken Object Level Authorization, API2 Broken Authentication, API3 Broken Object Property Level Authorization, API4 Unrestricted Resource Consumption, API5 Broken Function Level Authorization, API6 Unrestricted Access to Sensitive Business Flows, API7 Server Side Request Forgery, API8 Security Misconfiguration, API9 Improper Inventory Management, API10 Unsafe Consumption of APIs |
| OWASP Top 10 for LLM Applications 2025 | LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption |

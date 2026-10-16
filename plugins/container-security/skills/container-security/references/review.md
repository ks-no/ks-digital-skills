# Review of images and manifests

Load this file when the user asks for a review or an audit of a Dockerfile, a chart,
manifests or cluster commands.

## Scope

- For a branch or a pull request, review the changed files. Compare with the merge
  base of the default branch. Also read the files that the change uses, for example
  the values file of a chart, when you need them to judge a finding.
- Say at the start what you reviewed and what you did not review.

## Method

1. **Image.** Find the base images, the user, the files that the build copies, and
   each place where a secret can enter a layer.
2. **Workload.** For each container, find the security context, the volumes, the
   host settings and the user ID that the platform gives.
3. **Identity.** Find the ServiceAccount, its bindings and the verbs and resources
   that they allow. Find out what the app needs.
4. **Exposure.** Find the Services, Routes, Ingresses and NetworkPolicies, and who
   can reach each port.
5. **Secrets.** Follow each secret from where it is stored to where it is used.

## When to report a finding

Report a finding only when you can describe a concrete path from an attacker to an
impact, and you are at least 80% sure that it works. Name the attacker: anyone on
the internet, a user of the app, a person who can push an image or change the chart,
a process in a compromised container, or a user with access to the namespace.
Describe the path in words. Do not write a working exploit.

| Severity | Typical example |
| --- | --- |
| Critical | A container can take control of the node, or a workload has rights across the whole cluster. |
| High | A compromised container can read secrets of other workloads or change other workloads. A secret is in an image that other people can pull. |
| Medium | A token is mounted in a pod that does not use it, together with wide rights in the namespace. A base image or a tag that can change under a release. |
| Low | Hardening without a known attack path. |

Severity depends on the attacker and the impact, not on the type of setting.

## These are not findings

A setting that looks risky is a finding only if an attacker gets something from it.
Before you report a setting, find out what the platform does with it, and what an
attacker gains.

- A setting that is the documented mechanism of the platform for that concern, used
  as documented.
- A field that the file leaves out, when the platform or the admission control sets a
  safe value for it. Find out what the platform does before you report it as missing.
- Hardening that the reviewed files do not need for a known attack path, for example
  a missing NetworkPolicy in a change that does not touch the network. It is low, at
  most.
- Build hygiene, such as the image size, the stage layout or the order of the steps,
  when no secret and no build tool reaches the runtime image. It is low, at most.
- A risk that the reviewed files do not show. Do not report it. If your answer
  depends on it, add a `Check:` line.

When the files have no real problem, say so in one sentence. You can add up to three
low notes after it. Do not rewrite the files, and do not add new resources.

Hardening without an attack path is a note, not a finding. Put the notes after the
findings, one line each, without an attacker or a severity.

## Finding format

For each finding, give:

- **Title** and **severity** (critical, high, medium or low)
- **Location**: `file:line`. For pasted text without a file name, quote the line.
- **Attacker and path**: who can do it, and how, in two or three sentences
- **Impact**: what the attacker gets
- **Fix**: the smallest change that removes the problem. Keep the start command, the
  base image, the ports, the paths that the app writes and the API rights that the
  app uses. Use no value that you invented.
- **ID**: the OWASP risk and, if useful, the CWE

Start the report with one to three lines that give the result. Order the findings
from critical to low. If you find nothing, say "No findings", and list what you
checked. That is a valid result.

If a secret was in an image that was pushed, or in a committed file, say that the
secret must be rotated.

If your tool can start a separate agent with a fresh context, give it each critical
or high finding, and let it confirm or reject the finding. If not, check each one
again yourself against the list "These are not findings".

## OWASP IDs

Use the ID and the name. Do not copy text from OWASP.

| List | IDs |
| --- | --- |
| OWASP Kubernetes Top 10 (2025) | K01 Insecure Workload Configurations, K02 Overly Permissive Authorization Configurations, K03 Secrets Management Failures, K04 Lack Of Cluster Level Policy Enforcement, K05 Missing Network Segmentation Controls, K06 Overly Exposed Kubernetes Components, K07 Misconfigured And Vulnerable Cluster Components, K08 Cluster To Cloud Lateral Movement, K09 Broken Authentication Mechanisms, K10 Inadequate Logging And Monitoring |
| OWASP Top 10:2025 | A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions |

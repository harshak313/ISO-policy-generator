# ISMS-POL-INC-001: Incident & Threat Management Policy

**Document ID:** ISMS-POL-INC-001
**Document Name:** Incident & Threat Management Policy
**Version:** 1.0
**Date of Issue:** [Date]
**Document Owner:** [Owner]
**Approved By:** [Approver]
**Classification:** Internal
**Review Due Date:** [Date]

---

### 1. Purpose
The purpose of this policy is to ensure that [Organization Name] has a systematic and effective approach to managing information security threats and incidents. This policy aims to minimize the impact of security breaches, ensure a rapid and coordinated response, and facilitate continuous improvement of the Information Security Management System (ISMS) by learning from security events. This policy is established in accordance with the requirements of ISO/IEC 27001:2022.

### 2. Scope
This policy applies to all information security events and incidents affecting [Organization Name]’s assets, personnel, and third-party providers within the ISMS scope. It covers all digital and physical assets, including cloud services, endpoints, and network infrastructure, and applies to all employees, contractors, and external partners.

### 3. Definitions
*   **Information Security Event:** An identified occurrence of a security-related observation that may indicate a breach of security policy or a failure of security controls.
*   **Information Security Incident:** One or more information security events that have a significant impact on the organization's operations or security posture.
*   **Threat Intelligence:** Information relating to information security threats that is collected and analyzed to provide awareness and actionable insights.
*   **Evidence:** Data or physical objects that can be used to prove the occurrence of an event or incident, maintained in a manner that ensures admissibility in legal proceedings.
*   **CSIRT (Computer Security Incident Response Team):** A designated group of individuals responsible for responding to security incidents.

### 4. Roles and Responsibilities
*   **CISO:** Accountable for the overall incident management framework, approving the response plans, and overseeing the communication with authorities.
*   **CSIRT / Incident Response Team:** Responsible for the technical assessment, containment, eradication, and recovery from security incidents.
*   **IT Manager:** Responsible for providing technical logs, system access, and infrastructure support during an investigation.
*   **All Personnel:** Responsible for reporting any observed or suspected security events immediately through the approved channels.
*   **Legal/Compliance Officer:** Responsible for advising on regulatory notification requirements (e.g., GDPR, industry-specific laws).

### 5. Incident Identification and Reporting
[Organization Name] shall provide a clear and accessible mechanism for all personnel to report observed or suspected information security events in a timely manner.
*   **Reporting Channels:** Personnel shall report events via [Insert Channel, e.g., Security Portal, Dedicated Email, or Helpdesk].
*   **Reporting Requirements:** Reports should include the date/time of discovery, the nature of the event, the assets involved, and any immediate actions taken.
*   **Obligation:** All employees and contractors are contractually obligated to report security events; failure to do so may result in disciplinary action.

### 6. Incident Assessment and Classification
Upon receipt of a report, the CSIRT shall assess the event to determine if it constitutes an information security incident.
*   **Assessment Process:** The event is analyzed based on the impact on Confidentiality, Integrity, and Availability (CIA).
*   **Classification:** Incidents shall be categorized by severity:
    *   **Low:** Minimal impact on business operations; no sensitive data compromised.
    *   **Medium:** Moderate impact; localized disruption or potential exposure of non-critical data.
    *   **High:** Severe impact; critical system downtime or confirmed breach of sensitive/PII data.
    *   **Critical:** Catastrophic impact; widespread outage or massive data exfiltration.
*   **Decision:** A formal decision on whether an event is an "incident" shall be documented in the Incident Log.

### 7. Incident Response
All security incidents shall be responded to in accordance with the documented Incident Response Plan.
*   **Preparation:** The organization shall maintain updated contact lists, response toolkits, and communication templates.
*   **Containment:** Immediate actions shall be taken to limit the spread of the incident (e.g., isolating a network segment or disabling a compromised account).
*   **Eradication:** The root cause of the incident shall be identified and removed (e.g., deleting malware, patching a vulnerability).
*   **Recovery:** Systems shall be restored to normal operation, ensuring that the vulnerability is closed and integrity is verified.
*   **External Coordination:**
    *   **Authorities:** The CISO shall maintain established contacts with relevant law enforcement and regulatory authorities to be engaged during critical incidents.
    *   **Special Interest Groups:** The organization shall maintain memberships in security forums, ISACs, or professional associations to share and receive threat data.

### 8. Evidence Collection
To ensure the integrity of investigations and potential legal action, [Organization Name] shall implement procedures for the identification and preservation of evidence.
*   **Identification:** All volatile and non-volatile data (logs, memory dumps, disk images) related to the incident shall be identified.
*   **Acquisition:** Evidence shall be collected using forensically sound methods to prevent contamination.
*   **Preservation:** A Chain of Custody log shall be maintained, documenting who handled the evidence, when, and where it was stored.
*   **Storage:** Evidence shall be stored in a secure, access-controlled environment.

### 9. Lessons Learned
Following the closure of a major or high-severity incident, a Post-Incident Review (PIR) shall be conducted.
*   **Analysis:** The team shall analyze the timeline, the effectiveness of the response, and the root cause.
*   **Improvement:** Knowledge gained from the incident shall be used to strengthen existing controls and update the Risk Register (ISMS-RAT-001).
*   **Documentation:** A "Lessons Learned" report shall be produced and presented to the Information Security Board.

### 10. Monitoring and Enforcement
*   **Threat Intelligence:** The CISO and IT Manager shall collect and analyze information regarding current threats (via feeds, alerts, and forums) to proactively update security controls.
*   **Monitoring:** Incident response effectiveness shall be monitored through KPIs (e.g., Mean Time to Detect, Mean Time to Remediate).
*   **Enforcement:** Non-compliance with this policy, including failure to report incidents, will be handled according to the organization's disciplinary process.

### 11. Exceptions
Any exception to this policy must be formally requested, risk-assessed by the CISO, and approved in writing. Exceptions shall be reviewed every six months to determine if they are still required.

### 12. Compliance Requirements
This policy ensures compliance with:
*   ISO/IEC 27001:2022 Annex A controls.
*   Applicable data protection laws (e.g., GDPR, CCPA) regarding breach notification timelines.
*   Contractual obligations with clients regarding security incident reporting.

### 13. Review Requirements
This policy shall be reviewed at least annually or following a significant security incident. Reviews shall be conducted as part of the Management Review process to ensure the policy remains suitable and effective.

### 14. References
*   ISMS-POL-ISP-001: Information Security Policy
*   ISMS-POL-RSK-001: Risk Management Policy
*   ISMS-ROL-001: IS Roles & Responsibilities
*   ISO/IEC 27001:2022 Standard

---

### Appendix A - ISO 27001 Control Mapping

| ISO 27001:2022 Control | Control Title | Policy Section(s) |
| :--- | :--- | :--- |
| A.5.5 | Contact with authorities | 7. Incident Response |
| A.5.6 | Contact with special interest groups | 7. Incident Response |
| A.5.7 | Threat intelligence | 10. Monitoring and Enforcement |
| A.5.24 | Information security incident management planning and preparation | 4. Roles and Responsibilities, 7. Incident Response |
| A.5.25 | Assessment and decision on information security events | 6. Incident Assessment and Classification |
| A.5.26 | Response to information security incidents | 7. Incident Response |
| A.5.27 | Learning from information security incidents | 9. Lessons Learned |
| A.5.28 | Collection of evidence | 8. Evidence Collection |
| A.6.8 | Information security event reporting | 5. Incident Identification and Reporting |
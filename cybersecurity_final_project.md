# CYBERSECURITY FINAL PROJECT

**Title:** Secure Registration and Login System  
**Deadline:** June 3, 2026 (Anytime)  
**Submission Format:** Soft copy (folder with last name of group member as the folder name)

## 1. Project Overview

In this project, you will develop a secure user authentication system consisting of:
- Registration Module
- Login Module
- Password Strength Meter

Your system must implement cybersecurity techniques including:
- Hashing
- Salt
- Pepper
- Password Strength Validation

Additionally, your project must be:
- Hosted online using a Free Web Hosting Service
- Accessible through a public URL/link

You may use any programming language, framework, or database.

Examples:
- Languages/Frameworks: PHP, Python, Java, JavaScript, C#
- Databases: MySQL, SQLite, MongoDB

## 2. Learning Objectives

By completing this project, students should be able to:
- Understand password security concepts
- Implement secure password storage
- Apply hashing, salt, and pepper
- Develop secure authentication systems
- Validate password complexity using a password strength meter
- Deploy and host a web application online

## 3. System Requirements

### A. Registration Module

The registration form must include:
- Username
- Password
- Confirm Password

**Password Meter Requirements**

Your system must implement a Password Strength Meter that checks the following:

| Requirement | Description |
|---|---|
| Lowercase Letter | At least one lowercase letter |
| Uppercase Letter | At least one uppercase letter |
| Digit | At least one number |
| Symbol | At least one special character |
| Minimum Length | At least 12 characters |

**Example of Accepted Password:** Cyber@2026Secure  
**Example of Weak Password:** password123

**Password Meter Behavior**

The system should display password strength such as:
- Weak
- Medium
- Strong

| Password | Result |
|---|---|
| password | Weak |
| Password123 | Medium |
| Cyber@2026Secure | Strong |

**Registration Process**

During registration, the system must:
- Validate password strength.
- Generate a unique random salt.
- Combine: $\text{password} + \text{salt} + \text{pepper}$
- Apply a secure hashing algorithm.
- Store in the database:
  - Username
  - Password Hash
  - Salt

**Note:** The pepper must NOT be stored in the database.

### B. Login Module

The login module must:
- Accept:
  - Username
  - Password
- Retrieve the stored salt from the database.
- Recompute the hash using: $\text{input password} + \text{stored salt} + \text{pepper}$
- Compare the generated hash with the stored hash.
- Display:
  - Login Successful
  - Invalid Username or Password

### C. Online Hosting Requirement

Your Final Project must be hosted online using any Free Web Hosting Platform. Examples include:
- InfinityFree
- 000webhost
- AwardSpace
- FreeHosting
- Other free hosting services

Students may follow tutorials from YouTube for deployment and hosting (Free Web Hosting Tutorials on YouTube).

## 4. Security Requirements

Your project must demonstrate the following:

| Security Feature | Required |
|---|---|
| Password Hashing | Yes |
| Salt Implementation | Yes |
| Pepper Implementation | Yes |
| Password Meter | Yes |
| Minimum 12 Characters | Yes |
| Uppercase Validation | Yes |
| Lowercase Validation | Yes |
| Digit Validation | Yes |
| Symbol Validation | Yes |
| Plain Text Password Storage | X Not Allowed |

## 5. Required Outputs

### A. Screenshots

Provide screenshots showing:

**Registration Module:**
- Registration form
- Password meter
- Successful registration

**Login Module:**
- Successful login
- Failed login attempt

**Database/Table:**
- Show: Username, Password Hash, and Salt.
- Pepper should NOT appear in the database.

### B. Source Code

Submit complete source code including:
- Registration Module
- Login Module
- Password Meter
- Hashing Implementation
- Salt Generation
- Pepper Implementation

Code must:
- Be properly indented
- Include comments
- Be organized properly

### C. Short Documentation (1-3 Pages)

Your documentation must include:
- Hashing algorithm used
- How salt works
- How pepper works
- How password meter validates password strength
- Why strong passwords are important in cybersecurity
- Screenshot of the hosted online system
- Public URL or link of the hosted system (The hosted website link is a required part of the documentation.)

## 6. Suggested Folder Structure

```text
Final Project YourName/
├── screenshots/
├── source_code/
├── database/
├── documentation.pdf
└── hosted link.txt
```

## 7. Grading Criteria

| Criteria | Percentage |
|---|---:|
| Registration and Login Functionality | 25% |
| Correct Hash, Salt, and Pepper Implementation | 25% |
| Password Meter Implementation | 20% |
| Online Hosting and Accessibility | 15% |
| Code Quality and Organization | 10% |
| Documentation and Completeness | 5% |

## 8. Important Reminders

- Do NOT store passwords in plain text.
- Do NOT copy code from classmates.
- Use proper cybersecurity practices.
- Test your hosted system before submission.
- Ensure all submitted files are complete.
- Make sure your hosted system is accessible online.

## 9. Submission Details

**Deadline:** June 3, 2026 (Anytime)  
**Submit via:** (Instructor will specify platform)

## 10. Submission Note

**Note:** Include a cover page listing the names of all group members. Only one representative per group should submit the final project.

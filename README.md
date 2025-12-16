# Secure Inventory Management System

A web-based inventory management system built with Flask and SQLite, designed with
cybersecurity principles such as authentication, role-based access control, audit logging,
and secure session management.

This project demonstrates how security concepts can be applied in a real-world business
application rather than remaining purely theoretical.

---

## Live Demo

🔗 Live Site: 
🔗 GitHub Repository: (this repository)

---

## Security Features

- User authentication with securely hashed passwords (PBKDF2)
- Role-Based Access Control (admin vs staff)
- Admin-only inventory and user management
- Audit logging for inventory actions
- Session-based access enforcement
- Protection against direct URL privilege escalation

---

## Application Features

- Add, edit, delete inventory items (admin only)
- Category-based inventory organisation
- Expand/collapse category view
- Low-stock prioritisation and alerts
- Flash notifications for user actions
- Admin-only user creation and management

---

## Tech Stack

**Backend**
- Python
- Flask

**Frontend**
- HTML
- CSS
- JavaScript

**Database**
- SQLite

**Security**
- Werkzeug (password hashing)
- Flask Sessions

**DevOps**
- Git
- GitHub
- Render (deployment)

---

## Cybersecurity Concepts Demonstrated

- Authentication & Authorization
- Least Privilege
- Secure Credential Storage
- Accountability via Audit Logs
- Input Validation
- Secure Deployment Awareness

---

## ⚠️ Data Persistence Note

This project uses SQLite, which is suitable for local development and demonstration.
In cloud environments using ephemeral containers (such as Render free tier),
data persistence is not guaranteed.

**Planned Imp**

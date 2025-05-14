# 🧪 Test Log - Facebook Authentication Testing

## Test ID: TL-FB-002

### Test Case ID: TC-FB-SIGNUP-001

### Date: February 21, 2024

### Executed By: Dalonda Ikhimokpa

---

## Test Objective:

Verify signup form rejects invalid email formats.

---

## Test Steps:

1. Navigate to signup page
2. Enter "invalid-email" in email field
3. Complete other required fields
4. Click "Sign Up"

---

## Test Data:

- **Email:** invalid-email
- **Password:** Test123!
- **Browser:** Chrome 122

---

## Expected Result:

System should reject submission with email format error.

---

## Actual Result:

Test Failed: Form accepted invalid email format.

---

## Status: Fail

---

## Comments:

- No client-side validation for email field
- Server accepted malformed email
- Reported as BUG-FB-102 (Email validation missing)

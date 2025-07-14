# Golf Fundraiser Sweepstake Tournament App

## Overview
This Django web app manages a sweepstake for a golf tournament (e.g., The Open). It allows you to:
- Import contestants and their picks from an Excel sheet
- Track each contestant's 3 selected golfers and their odds
- Update player scores daily
- Automatically rank contestants by the combined score of their 3 golfers
- Manage all data via a simple web interface

## Features
- **Excel Import:** Upload an Excel file to bulk import contestants, their picks, and player odds.
- **Leaderboard:** View a ranked leaderboard of all contestants and their combined golfer scores.
- **Score Update:** Update all player scores from a single web form.
- **Admin Interface:** Full management of contestants, players, and picks.
- **Odds Validation:** Only allows picks with odds >= 100/1 (enforced in admin and import).

## Setup
1. Clone the repo and set up a Python virtual environment.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   pip install openpyxl
   ```
3. Run migrations:
   ```sh
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
4. Create a superuser:
   ```sh
   python3 manage.py createsuperuser
   ```
5. Start the server:
   ```sh
   python3 manage.py runserver
   ```

## URLs
- **Admin:** `/admin/` — Manage all data (requires login)
- **Admin Homepage:** `/sweepstake/admin-home/` — Staff-only dashboard
- **Leaderboard:** `/sweepstake/leaderboard/` — Public leaderboard of contestants and scores
- **Update Scores:** `/sweepstake/update-scores/` — Update all player scores (staff only)
- **Import Excel:** `/sweepstake/import-excel/` — Upload Excel file to import contestants and picks (staff only)
- **Reset Leaderboard:** `/sweepstake/reset-leaderboard/` — Delete all contestants and picks (staff only, destructive!)
- **Reset Golfers:** `/sweepstake/reset-players/` — Delete all golfers (players) (superuser only, destructive!)

## Excel Import Format
Your Excel file should have columns:

| Name | Payment Email | Created At | Phone Number | Select Golfer 1 | Golfer 1 odds | Select Golfer 2 | Golfer 2 odds | Select Golfer 3 | Golfer 3 odds |
|------|---------------|------------|--------------|------------------|---------------|------------------|---------------|------------------|---------------|

- Enter golfer names and odds in separate columns as shown above (e.g., `Ludvig Aberg` and `14/1`).
- "Created At" is used as a unique entry identifier.
- "Payment Email" is stored for each entry.

## How It Works
- Only the leaderboard is public. All other features are staff-only and require login. Reset Golfers is superuser-only.
- Each contestant must have 3 picks, each with odds >= 100/1 (enforced in admin and import).
- Player scores can be updated daily via the web form or admin.
- The leaderboard ranks contestants by the sum of their 3 golfers' scores (lower is better).
- Use the Reset Leaderboard feature to clear all entries and picks if you want to start over. **This is permanent!**

## Notes
- Only staff/admin users can import Excel or update scores.
- All contestant and player data can be managed via the Django admin.

---

For more details, see the code or contact the project maintainer. 
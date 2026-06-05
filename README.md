# Digital Graveyard Management

A comprehensive Django-based web application for managing and maintaining digital records of graveyards and cemetery sites.

**Live Demo:** https://digital-graveyard-management.onrender.com/

## Overview

The Digital Graveyard Management system is designed to provide an efficient and organized way to maintain records of burial sites, tombstones, and related cemetery information. This application leverages Django's robust framework combined with an SQL database to ensure data integrity and accessibility.

## Features

- **Digital Records Management**: Maintain comprehensive records of graves and cemetery sites
- **Database-Driven**: Uses SQL database for reliable data storage
- **Web-Based Interface**: Access cemetery records through a user-friendly web application
- **Django Framework**: Built on the secure and scalable Django framework

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (with SQL compatibility)
- **Deployment**: Render

## Project Structure

```
digitalgraveyardmanagement/
├── graveweb/              # Django app for graveyard web interface
├── web/                   # Additional web components
├── templates/             # HTML templates
├── staticfiles/           # Static files (CSS, JS, images)
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
├── requirements.txt       # Python dependencies
├── requirements-full.txt  # Full dependency list
├── Procfile               # Render deployment configuration
├── runtime.txt            # Python runtime specification
└── .gitignore             # Git ignore rules
```

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/preethamreddytn/digitalgraveyardmanagement.git
   cd digitalgraveyardmanagement
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## Deployment

This project is configured for deployment on Render. The `Procfile` and `runtime.txt` files contain the necessary deployment configuration.

### Deploy to Render

1. Push your changes to GitHub
2. Connect your repository to Render
3. Set up environment variables as needed
4. Deploy through Render's dashboard

## Usage

1. **Admin Panel**: Access the Django admin interface to manage records
2. **Web Interface**: Use the main web application to view and interact with graveyard records
3. **Database**: All records are stored securely in the SQL database

## Dependencies

Main dependencies (see `requirements.txt` for complete list):
- Django
- SQLAlchemy or Django ORM (for database operations)
- Gunicorn (for production server)

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for any improvements.

## License

This project is open source. See the LICENSE file for more information (if applicable).

## Author

**preethamreddytn**

- GitHub: https://github.com/preethamreddytn
- Repository: https://github.com/preethamreddytn/digitalgraveyardmanagement

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Last Updated**: June 2025

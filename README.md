# 📚 Telugu Digital Library

## About the Project
Telugu Digital Library is a web-based application developed to provide easy access to digital books.  
The application allows users to browse, search, and read books online through a clean and responsive user interface.

The system supports both **PDF-based books** and **HTML text-based books**, enabling an in-app reading experience without downloading files or opening external tabs.

This project is built using **Python (Flask)** for the backend and **SQLite** as the database, making it lightweight, fast, and easy to maintain.

---

## Project Objectives
- To create a simple and user-friendly digital books library
- To enable online reading of books within the application
- To manage book metadata using a database-driven approach
- To support multiple book formats (PDF and HTML)
- To demonstrate backend development skills using Flask and SQLite

---

## Project Specifications

### Functional Specifications
- Display a list of available books
- Search books by title or author
- Read books inside the application UI
- Support both PDF and HTML-based books
- Navigate easily between book list and reader pages
- Responsive design for desktop and mobile devices

---

### Book Management
Each book in the system contains:
- Title
- Author
- Language
- PDF file path (optional)
- HTML content or HTML file path (optional)

The system automatically decides how to render a book:
- If HTML content exists → open text reader
- Else if PDF exists → open PDF reader

---

### Reader Features
- In-app PDF reader using iframe
- In-app HTML text reader for page-style reading
- Back navigation to book list
- Clean and distraction-free reading interface

---

### Search Functionality
- Keyword-based search
- Case-insensitive search
- Search by title or author
- Uses GET method for bookmarkable searches

---

## Non-Functional Specifications

### Performance
- Fast response time for book listing and searching
- Efficient database queries using filtering

### Usability
- Simple and clean UI
- Easy navigation
- Mobile-friendly layout

### Security
- Server-side validation of file paths
- Controlled rendering of HTML content
- No direct access to local system files

### Maintainability
- Modular Flask routes
- Clear separation of frontend and backend
- Easy addition of new books without backend code changes

---

## Technologies Used
- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **Server:** Flask Development Server
- **OS:** Windows / Linux

---

## Project Scope

### In Scope
- Book listing and searching
- Online reading of PDF and HTML books
- Database-driven content management
- Responsive user interface
- Local deployment and testing
- Mobile access within the same network

---

### Out of Scope
- User authentication and login
- Payments or subscriptions
- User ratings or comments
- DRM or copyright enforcement
- Cloud storage integration
- Real-time analytics

---

## Future Enhancements
- Admin panel for adding books via UI
- Pagination for large book collections
- Dark mode reading experience
- Bookmarking and last-read position tracking
- Public online deployment
- Support for additional languages and formats

---

## Conclusion
The Telugu Digital Library project demonstrates practical backend and frontend development skills using Flask and SQLite.  
It provides a scalable foundation for a digital reading platform and can be enhanced with advanced features in the future.

---

## Author
Developed by S.VEERENDRA 

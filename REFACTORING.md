# Munra - Refactored Structure

## Project Structure

```
munra/
├── app.py              # Main application with routes
├── config.py           # Configuration constants
├── components.py       # Reusable UI components (NavBar, Footer, PostCard, etc.)
├── layouts.py          # Page layout templates
├── styles.py           # Global CSS styles with responsive design
├── utils.py            # SEO meta tags and utilities
├── data/
│   ├── __init__.py
│   ├── posts.py        # Post/notes data management
│   ├── machines.py     # Machine data
│   └── munras.py       # Munra (music releases) data management
└── static/
    ├── notes/          # Post content
    └── munras/         # Music releases
```

## Key Improvements

### 1. **Configuration Management**
- **config.py**: Centralized constants (colors, sizes, paths, copyright)
- Easy to update site-wide settings in one place
- No more hardcoded values scattered across files

### 2. **SEO & Meta Tags**
- **utils.py**: Generates Open Graph and Twitter Card meta tags
- Better social media sharing
- Proper viewport settings for mobile

### 3. **Responsive Design**
- Mobile-friendly layout (navbar becomes vertical on mobile)
- Grid adapts: 6 columns → 2 columns on mobile
- Typography scales down for smaller screens

### 4. **404 Error Page**
- Custom styled 404 page
- Consistent with site design
- Helpful navigation back to home

### 5. **Separation of Concerns**
- **app.py**: Only routes and high-level page logic
- **components.py**: Reusable UI components
- **layouts.py**: Page layout templates
- **styles.py**: Global styles
- **data/**: All data access logic

### 6. **DRY Principles**
- **TwoColumnLayout**: Eliminates repeated layout code across all pages
- **Footer**: Single component reused everywhere
- **PostCard & MachineCard**: Reusable card components
- **ContentSection**: Wrapper for content with consistent offset

## Critical Features Implemented

✅ **Configuration file** - All settings in one place  
✅ **404 page** - Custom error handling  
✅ **SEO meta tags** - Social media ready  
✅ **Responsive design** - Mobile friendly  
✅ **Constants** - No hardcoded values  

## Usage

### Adding a New Page

```python
@rt("/newpage")
def get():
    content = [
        H1("New Page"),
        ContentSection(
            P("Your content here")
        ),
    ]
    return TwoColumnLayout("newpage", content, "Page Title")
```

### Adding a New Component

Add to `components.py`:

```python
def NewComponent(data):
    return Div(
        # your component markup
    )
```

### Adding New Data

1. Create file in `data/` directory
2. Add data access functions
3. Import in `app.py` and use in routes

## Running the App

```bash
python3.14 app.py
```

The app will be available at http://localhost:5001

# EasyMeds - Flask Prototype

## Project Structure

```
EasyMeds/
│
├── app.py                        # Flask app entry point
├── templates/                   # HTML templates with Jinja
│   ├── base_with_nav.html       # Base layout with navigation bar
│   ├── base_no_nav.html         # Deprecated; replaced by refined layout
│   ├── index.html               # Landing page (with featured products)
│   ├── products.html            # All product listing page (full catalog)
│   ├── product_details.html     # Product detail view
│   ├── delivery_request.html    # Delivery request form (may be merged)
│   └── checkout.html            # Checkout summary (partial input fields)
│
├── static/
│   ├── css/
│   │   └── styles.css           # Custom styling overrides
│   └── img/                     # Product images
│       ├── Metformin.jpg
│       ├── Voltaren.jpg
│       ├── Burnaid.jpg
│       ├── Panadol.jpeg
│       └── Betadine.jpg
│
├── .gitignore                   # Prevent uploading cache, venv, etc
└── README.md                    # Project overview & instructions
```

---

## How to Run Locally
### 1. Install Flask (one-time setup)
```bash
pip install flask
```

### 2. Run the Server
```bash
python app.py
```
Default URL: `http://127.0.0.1:5000`

---

## Routing Overview (from app.py)
| Route | Function | HTML Template | Notes |
|-------|----------|----------------|-------|
| `/` | Home with featured products | `index.html` | Only shows a subset of key products |
| `/products` | All products catalog | `products.html` | Full listing with filter/sort controls |
| `/product/<product_id>` | Single Product Page | `product_details.html` | Renders detail by `product.id` |
| `/checkout` | Checkout Page | `checkout.html` | Combines delivery & payment fields |

---

## Feature Roadmap by Page

### `index.html`
- [x] Display limited featured products (currently all for demo)
- [ ] Add section title like "Popular Items" or "Featured Products"
- [ ] Add basic intro or welcome banner (e.g., hero section)

### `products.html`
- [x] Display all products from `products[]`
- [x] Filter by condition (dropdown - static, no JS)
- [x] Sort by price (Low-to-High / High-to-Low - static only)
- [ ] Optional: Add future category-based navigation (breadcrumb style)
- [ ] Add the long description down below

### `product_details.html`
- [x] Carousel for product images
- [x] Display usage, ingredients, and warning fields
- [ ] Improve visual layout: hierarchy of info & spacing

### `checkout.html`
- [x] Display mock cart content summary
- [ ] Add basic input fields (name, contact, delivery)
- [ ] Optional: Break down into step-by-step form (multi-section)

### `delivery_request.html`
- [ ] Consider merging with checkout or converting to a partial modal
- [ ] Otherwise, de-prioritize for now as checkout includes same inputs

---

## Notes
- All data currently stored in `products[]` inside `app.py`
- No JavaScript required this semester (HTML + Bootstrap only)
- Flask is used for routing and dynamic rendering
- Ensure image filenames match those listed in `products[]`

---

## Future Modularization Plan:
Currently, all logic is inside `app.py` for simplicity and easy onboarding.
As we integrate database and authentication features, we can modularize the app for better structure and maintainability:

- `routes/` → Route handlers (e.g., `main.py`, `auth.py`)
- `models.py` → Defines data structure (e.g., Product, User, using classes or ORM like SQLAlchemy)
- `forms.py` → Form validation using Flask-WTF
- `utils.py` or `db.py` → Helper functions or database interaction logic

This phased approach ensures that:
Beginners can quickly understand and contribute now
We retain long-term scalability when integrating advanced features later

---

## Collaboration Guidelines
- Work should be distributed by strength, not speed or assertiveness
- Coordinate via GitHub issues or shared tasks
- Avoid uncoordinated changes to shared files: `app.py`, `products[]`, or base templates
- Use `pull request` and `branch` flow if possible

### Suggested GitHub Workflow
- Clone the repo and create a branch (e.g., `products-page`, `checkout-form`)
- Add or modify templates / static files as needed
- Test changes locally with `python app.py`
- Commit with descriptive message and push to GitHub
- Open a PR for review or self-merge if trivial

---

Compiled by Peter Dong– for QUT IFN582 Flask Group Project (2025/05/06)

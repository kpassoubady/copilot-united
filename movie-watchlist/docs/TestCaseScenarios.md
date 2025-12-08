# Test Case Scenarios - Movie Watchlist Application

This document outlines integration test case scenarios and edge cases for the Movie Watchlist application.

## Table of Contents

1. [Movie CRUD Operations](#1-movie-crud-operations)
2. [Watchlist Operations](#2-watchlist-operations)
3. [Search and Filter Operations](#3-search-and-filter-operations)
4. [Frontend Routes](#4-frontend-routes)
5. [Database Operations](#5-database-operations)
6. [External API Integration](#6-external-api-integration)
7. [Edge Cases](#7-edge-cases)

---

## 1. Movie CRUD Operations

### 1.1 Create Movie

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-M-001 | Create movie with all fields | `{title: "Inception", year: 2010, genre: "Sci-Fi", description: "Dream heist movie"}` | Movie created successfully, returns movie object with ID | High |
| TC-M-002 | Create movie with only required field (title) | `{title: "Test Movie"}` | Movie created with null values for optional fields | High |
| TC-M-003 | Create movie with empty title | `{title: ""}` | Validation error, 422 status code | High |
| TC-M-004 | Create movie with very long title (>255 chars) | `{title: "A" * 300}` | Validation error or truncation | Medium |
| TC-M-005 | Create movie with invalid year (negative) | `{title: "Test", year: -2000}` | Validation error | Medium |
| TC-M-006 | Create movie with future year | `{title: "Test", year: 2050}` | Movie created (valid scenario) | Low |
| TC-M-007 | Create movie with year before cinema (< 1888) | `{title: "Test", year: 1800}` | Should validate or warn | Low |
| TC-M-008 | Create duplicate movie (same title/year) | Two movies with identical data | Both created (duplicates allowed) | Medium |

### 1.2 Read Movies

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-M-010 | Get all movies (empty database) | None | Empty list `[]` | High |
| TC-M-011 | Get all movies (with data) | None | List of all movies | High |
| TC-M-012 | Get movie by valid ID | `movie_id: 1` | Single movie object | High |
| TC-M-013 | Get movie by invalid ID | `movie_id: 99999` | 404 Not Found | High |
| TC-M-014 | Get movie by negative ID | `movie_id: -1` | 404 or 422 error | Medium |
| TC-M-015 | Get movie by non-integer ID | `movie_id: "abc"` | 422 Validation error | Medium |

### 1.3 Delete Movie

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-M-020 | Delete existing movie | `movie_id: 1` | Movie deleted, 200 OK | High |
| TC-M-021 | Delete non-existing movie | `movie_id: 99999` | 404 Not Found | High |
| TC-M-022 | Delete movie that is in watchlist | `movie_id` in watchlist | Movie and watchlist entry deleted | High |
| TC-M-023 | Delete same movie twice | Delete `movie_id: 1` twice | First succeeds, second returns 404 | Medium |

---

## 2. Watchlist Operations

### 2.1 Add to Watchlist

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-W-001 | Add movie to watchlist | `{movie_id: 1, user_notes: "Must watch!"}` | Watchlist item created | High |
| TC-W-002 | Add movie to watchlist without notes | `{movie_id: 1}` | Watchlist item created with null notes | High |
| TC-W-003 | Add non-existing movie to watchlist | `{movie_id: 99999}` | Error - Movie not found | High |
| TC-W-004 | Add duplicate movie to watchlist | Same movie_id twice | Error - Already in watchlist | High |
| TC-W-005 | Add movie with very long notes (>1000 chars) | `{movie_id: 1, user_notes: "A" * 2000}` | Should succeed or truncate | Medium |
| TC-W-006 | Add movie with special characters in notes | `{movie_id: 1, user_notes: "<script>alert('xss')</script>"}` | Notes sanitized/escaped | High |
| TC-W-007 | Add movie with emoji in notes | `{movie_id: 1, user_notes: "🎬 Great movie! 🍿"}` | Notes saved correctly | Low |

### 2.2 Read Watchlist

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-W-010 | Get empty watchlist | None | Empty list | High |
| TC-W-011 | Get watchlist with items | None | List with movie details | High |
| TC-W-012 | Watchlist item has correct movie reference | None | Each item includes full movie data | High |

### 2.3 Update Watchlist

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-W-020 | Toggle watched status (unwatched -> watched) | `item_id: 1` | `watched: 1` | High |
| TC-W-021 | Toggle watched status (watched -> unwatched) | `item_id: 1` | `watched: 0` | High |
| TC-W-022 | Update user notes | `{item_id: 1, user_notes: "Updated note"}` | Notes updated | High |
| TC-W-023 | Clear user notes | `{item_id: 1, user_notes: ""}` | Notes set to empty string | Medium |
| TC-W-024 | Update non-existing watchlist item | `item_id: 99999` | 404 or redirect | Medium |

### 2.4 Remove from Watchlist

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-W-030 | Remove existing item | `item_id: 1` | Item removed, redirect | High |
| TC-W-031 | Remove non-existing item | `item_id: 99999` | No error, redirect | Medium |
| TC-W-032 | Remove item, movie still exists | `item_id: 1` | Only watchlist entry removed | High |

---

## 3. Search and Filter Operations

### 3.1 Search

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-S-001 | Search with exact title match | `search: "Inception"` | Returns matching movie(s) | High |
| TC-S-002 | Search with partial title match | `search: "Incep"` | Returns movies containing "Incep" | High |
| TC-S-003 | Search case insensitive | `search: "INCEPTION"` | Returns "Inception" | High |
| TC-S-004 | Search with no results | `search: "xyznonexistent"` | Empty results, helpful message | High |
| TC-S-005 | Search with empty string | `search: ""` | Returns all movies | Medium |
| TC-S-006 | Search with special characters | `search: "<script>"` | Safe handling, no XSS | High |
| TC-S-007 | Search with SQL injection attempt | `search: "'; DROP TABLE movies;--"` | Safe handling, no SQL injection | High |
| TC-S-008 | Search with unicode characters | `search: "日本語"` | Handles unicode correctly | Low |

### 3.2 Filter by Genre

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-S-010 | Filter by existing genre | `genre: "Action"` | Returns only Action movies | High |
| TC-S-011 | Filter by non-existing genre | `genre: "NonExistent"` | Empty results | Medium |
| TC-S-012 | Filter genre case insensitive | `genre: "ACTION"` | Returns Action movies | Medium |
| TC-S-013 | Combined search and genre filter | `search: "Dark", genre: "Action"` | Returns movies matching both | High |

### 3.3 Sorting

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-S-020 | Sort by title ascending | `sort: "title"` | A-Z order | High |
| TC-S-021 | Sort by title descending | `sort: "title_desc"` | Z-A order | High |
| TC-S-022 | Sort by year newest first | `sort: "year_desc"` | Newest to oldest | High |
| TC-S-023 | Sort by year oldest first | `sort: "year"` | Oldest to newest | High |
| TC-S-024 | Sort with null years | `sort: "year"` | Null years handled (first or last) | Medium |
| TC-S-025 | Invalid sort parameter | `sort: "invalid"` | Default ordering or ignore | Low |

---

## 4. Frontend Routes

### 4.1 Page Rendering

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-F-001 | Home page loads | `GET /` | 200 OK, HTML with movie grid | High |
| TC-F-002 | Add movie page loads | `GET /add` | 200 OK, HTML with form | High |
| TC-F-003 | Movie detail page loads | `GET /movie/1` | 200 OK, HTML with movie details | High |
| TC-F-004 | Movie detail - invalid ID | `GET /movie/99999` | 404 page with error message | High |
| TC-F-005 | Watchlist page loads | `GET /watchlist` | 200 OK, HTML with watchlist | High |
| TC-F-006 | Static files served | `GET /static/css/styles.css` | 200 OK, CSS content | High |

### 4.2 Form Submissions

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-F-010 | Submit add movie form | POST form data | Redirect to home, movie added | High |
| TC-F-011 | Submit add movie with missing title | POST without title | Validation error | High |
| TC-F-012 | Submit add to watchlist | POST to `/watchlist/add/1` | Redirect to movie detail | High |
| TC-F-013 | Submit delete movie | POST to `/movie/1/delete` | Redirect to home | High |

---

## 5. Database Operations

### 5.1 Connection and Initialization

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-D-001 | Database initializes on startup | Application start | Tables created if not exist | High |
| TC-D-002 | Database file created in correct location | Application start | `data/movies.db` exists | High |
| TC-D-003 | Multiple concurrent connections | Parallel requests | No deadlocks or errors | Medium |

### 5.2 Data Integrity

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-D-010 | Watchlist references valid movie | Add watchlist item | Foreign key integrity maintained | High |
| TC-D-011 | Delete movie cascades to watchlist | Delete movie in watchlist | Watchlist entry also removed | High |
| TC-D-012 | Transaction rollback on error | Partial operation fails | No partial data saved | Medium |

---

## 6. External API Integration

### 6.1 API Service

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-A-001 | Fetch movie with valid API key | `api_key: "valid", title: "Inception"` | Movie data returned | High |
| TC-A-002 | Fetch movie with empty API key | `api_key: ""` | 400 error - API key required | High |
| TC-A-003 | Fetch movie with null API key | `api_key: None` | 400 error - API key required | High |
| TC-A-004 | API returns 404 | Movie not found | 404 error propagated | High |
| TC-A-005 | API returns 500 | Server error | 500 error propagated | Medium |
| TC-A-006 | API timeout | Slow response | Timeout handled gracefully | Medium |
| TC-A-007 | API response cached | Same request twice | Second uses cache | Low |

### 6.2 Fanart Service

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-A-010 | Get poster for valid TMDB ID | `tmdb_id: 27205` | Poster URL returned | Medium |
| TC-A-011 | Get poster for invalid TMDB ID | `tmdb_id: 99999999` | None returned | Medium |
| TC-A-012 | Get poster with null TMDB ID | `tmdb_id: None` | None returned | Medium |
| TC-A-013 | Fanart API timeout | Slow response | Graceful fallback | Low |
| TC-A-014 | Poster caching works | Same TMDB ID twice | LRU cache used | Low |

---

## 7. Edge Cases

### 7.1 Boundary Conditions

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-E-001 | Maximum movies in database | 10,000+ movies | Performance acceptable | Low |
| TC-E-002 | Maximum watchlist items | 1,000+ items | Performance acceptable | Low |
| TC-E-003 | Year at boundary (1888) | `year: 1888` | First film year accepted | Low |
| TC-E-004 | Year at boundary (current year) | `year: 2024` | Accepted | Low |
| TC-E-005 | Empty database operations | All operations on empty DB | Graceful handling | High |

### 7.2 Concurrent Operations

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-E-010 | Simultaneous movie additions | 10 concurrent POSTs | All succeed without conflict | Medium |
| TC-E-011 | Read while writing | GET during POST | No dirty reads | Medium |
| TC-E-012 | Delete during read | DELETE while GET in progress | Consistent state | Medium |

### 7.3 Error Handling

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-E-020 | Database connection lost | DB file deleted | Graceful error message | Medium |
| TC-E-021 | Invalid JSON in request | Malformed JSON body | 422 error with details | High |
| TC-E-022 | Missing required headers | No Content-Type | Appropriate error | Medium |
| TC-E-023 | Request body too large | >10MB payload | 413 error | Low |

### 7.4 Security Edge Cases

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-E-030 | XSS in movie title | `title: "<script>alert(1)</script>"` | Escaped in output | High |
| TC-E-031 | XSS in user notes | `notes: "<img onerror='alert(1)'>"` | Escaped in output | High |
| TC-E-032 | Path traversal in static files | `GET /static/../../../etc/passwd` | 404 or 403 | High |
| TC-E-033 | CSRF on form submission | POST without valid origin | Should have CSRF protection | Medium |

### 7.5 Data Validation Edge Cases

| Test ID | Scenario | Input | Expected Result | Priority |
|---------|----------|-------|-----------------|----------|
| TC-E-040 | Whitespace-only title | `title: "   "` | Validation error or trimmed | High |
| TC-E-041 | Title with only special chars | `title: "!@#$%^&*()"` | Accepted (valid title) | Low |
| TC-E-042 | Extremely long description | 10,000+ characters | Accepted or truncated | Low |
| TC-E-043 | Null bytes in string | `title: "Test\x00Movie"` | Sanitized | Medium |
| TC-E-044 | Unicode normalization | Different unicode forms | Consistent handling | Low |

---

## Test Data Requirements

### Sample Movies for Testing

```python
TEST_MOVIES = [
    {"title": "Test Movie 1", "year": 2020, "genre": "Action", "description": "Test description"},
    {"title": "Test Movie 2", "year": 2021, "genre": "Comedy", "description": "Another test"},
    {"title": "Edge Case Movie", "year": None, "genre": None, "description": None},
    {"title": "A" * 255, "year": 1888, "genre": "Drama", "description": "Boundary test"},
]
```

### Test Database Setup

```python
# Fixture for clean test database
@pytest.fixture
def test_db():
    # Create in-memory SQLite database
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
```

---

## Test Execution Priority

| Priority | Description | When to Run |
|----------|-------------|-------------|
| **High** | Critical functionality, security | Every commit, PR |
| **Medium** | Important features, edge cases | Daily, before release |
| **Low** | Performance, rare scenarios | Weekly, release candidates |

---

## Integration Test Implementation Notes

1. **Use `TestClient`** from FastAPI for HTTP-level integration tests
2. **Use in-memory SQLite** for test isolation
3. **Mock external APIs** (fanart.tv, movie API) to avoid rate limits
4. **Reset database state** between tests using fixtures
5. **Use `pytest-asyncio`** for async endpoint testing
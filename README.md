# Chitter Challenge

## User Stories
> As a Maker        
> So that I can let people know what I am doing     
> I want to post a message (peep) to chitter        

> As a maker        
> So that I can see what others are saying      
> I want to see all peeps in reverse chronological order        

> As a Maker        
> So that I can better appreciate the context of a peep     
> I want to see the time at which it was made       

## Routes
/home => GET
/new => GET
/home => POST

## Pages
```html
<!-- GET /home -->
 <!DOCTYPE html>
 <html>
    <head>
        <title>Chitter</title>
        <meta charset='utf-8'>
    </head>
    <body>
        <h1>Chitter</h1>
        <a href='/new'>Write a Peep!</a>

        <h2>Chitter Feed</h2>
        <div>
            <!-- posts listed newest to oldest -->
            <!-- timestamp for each individual post -->
        </div>
    </body>
 </html>
```

```html
<!-- GET /new -->
 <!DOCTYPE html>
 <html>
    <head>
        <title>Chitter: New Post</title>
        <meta charset='utf-8'>
    </head>
    <body>
        <h1>New Peep</h1>
        <form action='/home' method='POST'>
            <label for='author-name'>Peeper:</label>
            <input type='text' name='author-name' id='author-name'>
            <label for='new-peep'>Your Peep:</label>
            <input type='text' name='new-peep' id='new-peep'>

            <input type='submit' value='Peep!'>
        </form>
 </html>
```
## Methods required
- All() => SELECT * FROM peeps;
- Create() => INSERT INTO peeps (%s) VALUES (%s)

## Class Interface (High-Level)
**Model Class**
```py
# lib/models/peep.py
class Peep:
    pass
```
**Repository Class**
```py
# lib/repositories/peep_repository.py
class PeepRepository:
    pass
```

## Database Design
DB name: **chitter_challenge**

### Basic Schema

```bash
table: peeps

columns: id | author? | peep | timestamp
```

### Table
```sql
CREATE TABLE peeps (
    id PRIMARY KEY SERIAL,
    author VARCHAR(255) NOT NULL,
    peep TEXT NOT NULL,
    time_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Test data**
```sql
INSERT INTO peeps (author, peep) VALUES (
    ('test author_1', 'this is a test peep'),
    ('test author_2', 'this is another test peep')
);
```



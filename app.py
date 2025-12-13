from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
@app.route('/')
def index():
    category = request.args.get('category')

    conn = get_db_connection()

    # Get distinct categories for dropdown
    categories = conn.execute(
        'SELECT DISTINCT category FROM inventory'
    ).fetchall()

    if category:
        items = conn.execute(
            '''
            SELECT *,
            CASE
                WHEN quantity <= min_level THEN "LOW"
                ELSE "OK"
            END AS status
            FROM inventory
            WHERE category = ?
            ''',
            (category,)
        ).fetchall()
    else:
        items = conn.execute(
            '''
            SELECT *,
            CASE
                WHEN quantity <= min_level THEN "LOW"
                ELSE "OK"
            END AS status
            FROM inventory
            '''
        ).fetchall()

    conn.close()

    return render_template(
        'index.html',
        items=items,
        categories=categories,
        selected_category=category
    )



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_stock(id):
    conn = get_db_connection()

    item = conn.execute(
        'SELECT * FROM inventory WHERE id = ?',
        (id,)
    ).fetchone()

    error = None

    if request.method == 'POST':
        action = request.form['action']
        amount = int(request.form['amount'])

        if action == 'used':
            if amount > item['quantity']:
                error = "Not enough stock available."
            else:
                conn.execute(
                    'UPDATE inventory SET quantity = quantity - ? WHERE id = ?',
                    (amount, id)
                )
        else:
            conn.execute(
                'UPDATE inventory SET quantity = quantity + ? WHERE id = ?',
                (amount, id)
            )

        if error is None:
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    conn.close()
    return render_template('update_stock.html', item=item, error=error)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        unit = request.form['unit']
        min_level = int(request.form['min_level'])

        conn.execute(
            '''
            UPDATE inventory
            SET name = ?, category = ?, unit = ?, min_level = ?
            WHERE id = ?
            ''',
            (name, category, unit, min_level, id)
        )

        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    item = conn.execute(
        'SELECT * FROM inventory WHERE id = ?',
        (id,)
    ).fetchone()

    conn.close()
    return render_template('edit_item.html', item=item)
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        quantity = int(request.form['quantity'])
        unit = request.form['unit']
        min_level = int(request.form['min_level'])

        conn = get_db_connection()
        conn.execute(
            '''
            INSERT INTO inventory (name, category, quantity, unit, min_level)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (name, category, quantity, unit, min_level)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('add_item.html')
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_item(id):
    conn = get_db_connection()

    if request.method == 'POST':
        conn.execute(
            'DELETE FROM inventory WHERE id = ?',
            (id,)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    item = conn.execute(
        'SELECT * FROM inventory WHERE id = ?',
        (id,)
    ).fetchone()
    conn.close()

    return render_template('delete_item.html', item=item)

if __name__ == '__main__':
    app.run

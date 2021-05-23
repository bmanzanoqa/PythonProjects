from application import app

print("Running your MICEX")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

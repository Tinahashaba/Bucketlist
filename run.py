from app import app

app.secret_key = "jfhjeeurhfjfieoosjdjdkiosooalaks0wssjsjk"
app.config['SESSION_TYPE'] = 'filesystem'

# Running the application
if __name__ == '__main__':
    app.run(debug=True)

from app import app



# Running the application
if __name__ == '__main__':
    app.secret_key = "jfhjeeurhfjfieoosjdjdkiosooalaks0wssjsjk"
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)

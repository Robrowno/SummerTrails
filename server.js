require('dotenv').config();

const express = require('express');
const mongoose = require('mongoose');
const { User, Image, Geolocation } = require('./schema');
const passport = require('./auth'); // Import the authentication code from auth.js
const session = require('express-session');
const bcrypt = require('bcrypt');
const { v4: uuidv4 } = require('uuid');

const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Session and Passport Configuration
app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false
}));

app.use(passport.initialize());
app.use(passport.session());

// Routes
app.get('/', (req, res) => {
    res.send('Hello World!');
});

// Connect to the Database
const dbURL = process.env.DB_URL;
mongoose
    .connect(dbURL, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to database'))
    .catch(err => console.log('Failed to connect to database', err));

// Authentication
const isAuthenticated = (req, res, next) => {
    if (req.isAuthenticated()) {
        return next();
    }

    res.redirect('/login');
};

app.post('/login', passport.authenticate('local', {
    successRedirect: '/dashboard',
    failureRedirect: '/login',
}));

app.get('/dashboard', isAuthenticated, (req, res) => {
    res.send('Welcome to the dashboard!');
});

app.get('/logout', (req, res) => {
    req.logout();
    res.redirect('/login');
});

app.post('/register', async (req, res) => {
    const { email, password } = req.body;
  
    try {
      const hashedPassword = await bcrypt.hash(password, 10);
  
      const newUser = new User({
        id: uuidv4(),
        authentication: { email, password: hashedPassword }
      });
  
      await newUser.save();
  
      res.redirect('/dashboard');
    } catch (error) {
      console.error('Failed to register user:', error);
      res.status(500).send('Internal Server Error');
    }
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

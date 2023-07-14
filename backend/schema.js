const mongoose = require('mongoose');
const { Schema } = mongoose;

// userSchema stores the user's id and authentication information
const userSchema = new Schema({
    _id: { type: Schema.Types.ObjectId, auto: true },
    authentication: { type: Schema.Types.Mixed },
    created_at: { type: Date, default: Date.now },
    modified_on: { type: Date, default: Date.now },
});

// imageSchema stores the image's id, user_id, upload_image, title, description, date, created_at, modified_on, approved, and likes
const imageSchema = new Schema({
    id: { type: String, required: true, unique: true },
    user_id: { type: Schema.Types.ObjectId, ref: 'User' },
    upload_image: { type: String },
    title: { type: String },
    description: { type: String },
    date: { type: Date },
    created_at: { type: Date, default: Date.now },
    modified_on: { type: Date, default: Date.now },
    approved: { type: Boolean, default: false },
    likes: { type: Number, default: 0 },
});

// geolocationSchema stores the geolocation's id, user_id, latitude, longitude, created_at, and modified_on
const geolocationSchema = new Schema({
    id: { type: String, required: true, unique: true },
    user_id: { type: Schema.Types.ObjectId, ref: 'User' },
    latitude: { type: Number },
    longitude: { type: Number },
    created_at: { type: Date, default: Date.now },
    modified_on: { type: Date, default: Date.now },
});

// User, Image, and Geolocation are models that use the schemas above
const User = mongoose.model('User', userSchema);
const Image = mongoose.model('Image', imageSchema);
const Geolocation = mongoose.model('Geolocation', geolocationSchema);

module.exports = { User, Image, Geolocation };

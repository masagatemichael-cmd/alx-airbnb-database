-- AirBnB Sample Data
-- Seed data for testing and development

-- Insert sample users
INSERT INTO users (user_id, first_name, last_name, email, password_hash, phone_number, role) VALUES
    (uuid_generate_v4(), 'John', 'Smith', 'john.smith@example.com', 'hashed_password_123', '+1234567890', 'host'),
    (uuid_generate_v4(), 'Sarah', 'Johnson', 'sarah.j@example.com', 'hashed_password_123', '+1234567891', 'host'),
    (uuid_generate_v4(), 'Mike', 'Brown', 'mike.brown@example.com', 'hashed_password_123', '+1234567892', 'guest'),
    (uuid_generate_v4(), 'Emily', 'Davis', 'emily.davis@example.com', 'hashed_password_123', '+1234567893', 'guest'),
    (uuid_generate_v4(), 'Admin', 'User', 'admin@airbnb.com', 'hashed_password_123', '+1234567894', 'admin');

-- Insert sample properties
INSERT INTO properties (property_id, host_id, name, description, location, price_per_night) 
SELECT 
    uuid_generate_v4(),
    (SELECT user_id FROM users WHERE email = 'john.smith@example.com'),
    'Cozy Downtown Apartment',
    'Beautiful apartment in the heart of the city with modern amenities and great views.',
    'New York, NY',
    120.00
WHERE NOT EXISTS (SELECT 1 FROM properties WHERE name = 'Cozy Downtown Apartment');

INSERT INTO properties (property_id, host_id, name, description, location, price_per_night) 
SELECT 
    uuid_generate_v4(),
    (SELECT user_id FROM users WHERE email = 'john.smith@example.com'),
    'Beachfront Villa',
    'Stunning villa with private beach access, ocean views, and luxury amenities.',
    'Miami, FL',
    250.00
WHERE NOT EXISTS (SELECT 1 FROM properties WHERE name = 'Beachfront Villa');

INSERT INTO properties (property_id, host_id, name, description, location, price_per_night) 
SELECT 
    uuid_generate_v4(),
    (SELECT user_id FROM users WHERE email = 'sarah.j@example.com'),
    'Mountain Cabin Retreat',
    'Peaceful cabin in the mountains with hiking trails and nature views.',
    'Denver, CO',
    95.00
WHERE NOT EXISTS (SELECT 1 FROM properties WHERE name = 'Mountain Cabin Retreat');

INSERT INTO properties (property_id, host_id, name, description, location, price_per_night) 
SELECT 
    uuid_generate_v4(),
    (SELECT user_id FROM users WHERE email = 'sarah.j@example.com'),
    'Luxury City Condo',
    'Modern condo in city center with pool, gym, and stunning city views.',
    'Los Angeles, CA',
    180.00
WHERE NOT EXISTS (SELECT 1 FROM properties WHERE name = 'Luxury City Condo');

-- Insert sample bookings
INSERT INTO bookings (booking_id, property_id, user_id, start_date, end_date, total_price, status) 
SELECT 
    uuid_generate_v4(),
    (SELECT property_id FROM properties WHERE name = 'Cozy Downtown Apartment'),
    (SELECT user_id FROM users WHERE email = 'mike.brown@example.com'),
    CURRENT_DATE + INTERVAL '10 days',
    CURRENT_DATE + INTERVAL '15 days',
    600.00,
    'confirmed'
WHERE NOT EXISTS (SELECT 1 FROM bookings LIMIT 1);

INSERT INTO bookings (booking_id, property_id, user_id, start_date, end_date, total_price, status) 
SELECT 
    uuid_generate_v4(),
    (SELECT property_id FROM properties WHERE name = 'Beachfront Villa'),
    (SELECT user_id FROM users WHERE email = 'emily.davis@example.com'),
    CURRENT_DATE + INTERVAL '20 days',
    CURRENT_DATE + INTERVAL '25 days',
    1250.00,
    'pending'
WHERE (SELECT COUNT(*) FROM bookings) = 1;

-- Insert sample payments
INSERT INTO payments (payment_id, booking_id, amount, payment_method) 
SELECT 
    uuid_generate_v4(),
    (SELECT booking_id FROM bookings WHERE total_price = 600.00),
    600.00,
    'credit_card'
WHERE NOT EXISTS (SELECT 1 FROM payments LIMIT 1);

-- Insert sample reviews
INSERT INTO reviews (review_id, property_id, user_id, rating, comment) 
SELECT 
    uuid_generate_v4(),
    (SELECT property_id FROM properties WHERE name = 'Cozy Downtown Apartment'),
    (SELECT user_id FROM users WHERE email = 'mike.brown@example.com'),
    5,
    'Amazing apartment! Great location and very clean. Would definitely stay again.'
WHERE NOT EXISTS (SELECT 1 FROM reviews LIMIT 1);

INSERT INTO reviews (review_id, property_id, user_id, rating, comment) 
SELECT 
    uuid_generate_v4(),
    (SELECT property_id FROM properties WHERE name = 'Mountain Cabin Retreat'),
    (SELECT user_id FROM users WHERE email = 'emily.davis@example.com'),
    4,
    'Beautiful cabin with amazing views. Very peaceful and relaxing stay.'
WHERE (SELECT COUNT(*) FROM reviews) = 1;

-- Insert sample messages
INSERT INTO messages (message_id, sender_id, recipient_id, message_body) 
SELECT 
    uuid_generate_v4(),
    (SELECT user_id FROM users WHERE email = 'mike.brown@example.com'),
    (SELECT user_id FROM users WHERE email = 'john.smith@example.com'),
    'Hi John, I am interested in your downtown apartment. Is it available next weekend?'
WHERE NOT EXISTS (SELECT 1 FROM messages LIMIT 1);

INSERT INTO messages (message_id, sender_id, recipient_id, message_body, is_read) 
SELECT 
    uuid_generate_v4(),
    (SELECT user_id FROM users WHERE email = 'john.smith@example.com'),
    (SELECT user_id FROM users WHERE email = 'mike.brown@example.com'),
    'Hi Mike! Yes, the apartment is available next weekend. Would you like to book it?',
    true
WHERE (SELECT COUNT(*) FROM messages) = 1;

-- Display sample data counts
SELECT 
    (SELECT COUNT(*) FROM users) as user_count,
    (SELECT COUNT(*) FROM properties) as property_count,
    (SELECT COUNT(*) FROM bookings) as booking_count,
    (SELECT COUNT(*) FROM payments) as payment_count,
    (SELECT COUNT(*) FROM reviews) as review_count,
    (SELECT COUNT(*) FROM messages) as message_count;
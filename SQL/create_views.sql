CREATE OR REPLACE VIEW booking_view AS
SELECT
  b.booking_id,
  g.first_name,
  g.phone_number,
  r.room_number,
  b.status
FROM booking_booking b
JOIN booking_guest g ON b.guest_id = g.phone_number
JOIN booking_room r ON b.room_id = r.room_number;

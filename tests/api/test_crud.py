import pytest
from core.api.client import AsyncAPIClient
from data.models import BookingDates, BookingRequest, BookingResponse

@pytest.mark.asyncio
async def test_complete_booking_lifecycle():
    api = AsyncAPIClient()

    # 1. SETUP: Auth & Data using Pydantic Models
    token = await api.get_token()
    dates = BookingDates(checkin="2027-05-01", checkout="2027-05-10")
    request_data = BookingRequest(
        firstname="Fname",
        lastname="Lname",
        totalprice=500,
        depositpaid=True,
        bookingdates=dates,
        additionalneeds="Late Check-in"
    )

    # 2. CREATE
    create_res = await api.create_booking(booking_data=request_data)
    booking_id = create_res.json()["bookingid"]
    # Create Verification
    assert create_res.status_code == 200
    # Validate the entire response structure using Pydantic
    booking_res = BookingResponse(**create_res.json())
    assert booking_res.bookingid > 0
    assert booking_res.booking.firstname == "Fname"
    print(f"\n✅ Created Booking ID: {booking_res.bookingid}")

    # 3. UPDATE
    request_data.firstname = "Fname-Updated"
    update_req = await api.update_booking(booking_id=booking_id, booking_data=request_data, token=token)
    # Update Verification
    assert update_req.status_code == 200
    assert update_req.json()["firstname"] == "Fname-Updated"
    print(f"\n✅ Successfully Updated Booking {booking_id} using Token!")

    # 4. DELETE
    delete_res = await api.delete_booking(booking_id=booking_id, token=token)
    # Delete Verification
    assert delete_res.status_code == 201 # Restful-booker returns 201 Created for a successful delete
    print(f"\n🗑️ Successfully Deleted Booking {booking_id}. Database is clean!")

    # 5. CLOSE SESSION
    await api.close()
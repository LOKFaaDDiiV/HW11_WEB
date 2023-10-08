from datetime import datetime, timedelta
from typing import List

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel, ContactUpdate


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(name=body.name, lastname=body.lastname, email=body.email, phone=body.phone, birth_date=body.birth_date)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        # tags = db.query(Tag).filter(Tag.id.in_(body.tags)).all()
        contact.name = body.name
        contact.lastname = body.lastname
        contact.email = body.email
        contact.phone = body.phone
        contact.birth_date = body.birth_date
        db.commit()
    return contact


async def find_contacts(db: Session, name: str = None, lastname: str = None, email: str = None) -> List[Contact]:
    q = None
    if name:
        q = db.query(Contact).filter(Contact.name.ilike(f"%{name}%"))
    if lastname:
        q = db.query(Contact).filter(Contact.lastname.ilike(f"%{lastname}%"))
    if email:
        q = db.query(Contact).filter(Contact.email.ilike(f"%{email}%"))
    if q is not None:
        contact = q.all()
        return contact
    else:
        return q


async def get_birthdays(num_days: int, db: Session) -> List[Contact]:

    contacts = db.query(Contact).all()
    today = datetime.now().date()
    end_date = today + timedelta(days=num_days)
    nearest_birthdays = []

    for contact in contacts:

        contact_birth_in_this_year = contact.birth_date.replace(year=today.year)

        if today <= contact_birth_in_this_year <= end_date:
            nearest_birthdays.append(contact)

    return nearest_birthdays

from models.book import Book
from models.loan import Loan
from models.member import Member

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. List all books")
        print("3. Find a book by title")
        print("4. Delete a book by ISBN")
        print("5. Add a member")
        print("6. List all members")
        print("7. Find a member by name")
        print("8. Delete a member by email")
        print("9. Loan a book")
        print("10. List all loans")
        print("11. Return a book")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            Book.create(title, author, isbn)
            print("Book added successfully.")
        elif choice == "2":
            books = Book.select()
            for book in books:
                print(book)
            print("Books listed successfully.")
        elif choice == "3":
            title = input("Enter the title to search for: ")
            books = Book.find_by_title(title)
            for book in books:
                print(book)
            print("Book search completed successfully.")
        elif choice == "4":
            isbn = input("Enter the ISBN of the book to delete: ")
            book = Book.find_by_isbn(isbn)
            if book:
                book.delete()
                print("Book deleted successfully.")
            else:
                print("Book not found.")
        elif choice == "5":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            Member.create(name, email)
            print("Member added successfully.")
        elif choice == "6":
            members = Member.select()
            for member in members:
                print(member)
            print("Members listed successfully.")
        elif choice == "7":
            name = input("Enter the name to search for: ")
            members = Member.find_by_name(name)
            for member in members:
                print(member)
            print("Member search completed successfully.")
        elif choice == "8":
            email = input("Enter the email of the member to delete: ")
            member = Member.find_by_email(email)
            if member:
                member.delete()
                print("Member deleted successfully.")
            else:
                print("Member not found.")
        elif choice == "9":
            book_id = int(input("Enter the book ID: "))#int converts string to an integer
            member_id = int(input("Enter the member ID: "))
            loan_date = input("Enter the loan date (YYYY-MM-DD): ")
            return_date = input("Enter the return date (YYYY-MM-DD): ")
            Loan.create(book_id, member_id, loan_date, return_date)
            print("Book loaned successfully.")
        elif choice == "10":
            loans = Loan.select()
            for loan in loans:
                print(loan)
            print("Loans listed successfully.")
        elif choice == "11":
            loan_id = int(input("Enter the loan ID to return: "))
            loan = Loan.find_by_id(loan_id)
            if loan:
                loan.delete()
                print("Book returned successfully.")
            else:
                print("Loan not found.")
        elif choice == "12":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

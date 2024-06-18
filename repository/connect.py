import asyncio
from sqlalchemy import Table, Column, Integer, String, MetaData
from databases import Database
from sqlalchemy import select

# Define metadata
metadata = MetaData()

# Define the quiz table
quiz_table = Table(
    'quiz', metadata,
    Column('id', Integer),
    Column('user_id', Integer),
)

# Connect to the database
DATABASE_URL = "mysql://root:123456@localhost/test_2"
database = Database(DATABASE_URL)

# Function to execute queries
async def execute_query(user_id):
    try:
        # Mở kết nối đến cơ sở dữ liệu
        await database.connect()

        # Tạo câu truy vấn để lấy dữ liệu từ bảng
        query = select(quiz_table.c.id).where(quiz_table.c.user_id == user_id)

        # Thực hiện truy vấn và lấy kết quả
        record_id = await database.fetch_all(query)

        # Đóng kết nối đến cơ sở dữ liệu
        await database.disconnect()
        ids = [record.id for record in record_id]
        return ids
    except Exception as e:
        return f"Error saving quiz to database: {str(e)}"



# Example of querying all rows from the quiz table
async def fetch_all_quiz_records():
    query = quiz_table.select()
    records = await execute_query(query)
    return [dict(record) for record in records]

# Function to save quiz data to the database
async def save_quiz_to_database(quiz_id):
    try:
        # Mở kết nối đến cơ sở dữ liệu
        await database.connect()

        # Thực hiện thao tác trong một transaction
        async with database.transaction():
            await database.execute(
                quiz_table.insert().values(
                    id=quiz_id,
                    user_id=1
                )
            )
        # Đóng kết nối
        await database.disconnect()
        return "success"
    except Exception as e:
        return f"Error saving quiz to database: {str(e)}"


# Cleanup function to disconnect from the database
async def cleanup():
    await database.disconnect()

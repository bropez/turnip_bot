import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('turnip_tracker').sheet1


def insert_name(name: str):
    sheet.append_row([name])


def get_row(name: str):
    try:
        cell = sheet.find(name)
    except gspread.exceptions.CellNotFound:
        insert_name(name)
        cell = sheet.find(name)

    return cell.row


def get_col(day_and_time: str):
    cell = sheet.find(day_and_time)
    return cell.col


def update_row_col(name: str, day_and_time: str, price: int):
    row = get_row(name)
    col = get_col(day_and_time)

    sheet.update_cell(row, col, price)
    print("finished updating cell {},{} for {}".format(row, col, name))


if __name__ == '__main__':
    name = 'matthewmatthew'
    day_and_time = 'tuesday_am'
    price = 50
    update_row_col(name, day_and_time, price)

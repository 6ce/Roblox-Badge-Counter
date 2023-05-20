import requests as Requests, os as OS

print("Input UserID below:")
UserID = str(input("\n"))

if OS.name == "posix":
	ClearConsole = "clear"
elif OS.name == "nt":
	ClearConsole = "cls"

OS.system(ClearConsole)

if UserID.isnumeric() == False:
	raise Exception("Invalid UserID")

BadgesUrl = f"https://badges.roblox.com/v1/users/{UserID}/badges?limit=100&sortOrder=Asc"
UsersUrl = f"https://users.roblox.com/v1/users/{UserID}"

Cursor = ""
Pages = []
Threads = []

CurrentPage = 0
TotalBadges = 0
ThreadsStarted = 0

AccInfo = Requests.get(UsersUrl).json()

while True:
	print(f"On page: {str(CurrentPage)} - Current Badge Amount: {str(TotalBadges)}")

	CurrentPage += 1

	if Cursor == "":
		Response = Requests.get(BadgesUrl).json()
		Page = Response["data"]
		Cursor = Response["nextPageCursor"]

		Pages.append(Page)
		TotalBadges += len(Page)
	elif Cursor != None:
		Response = Requests.get(f"{BadgesUrl}&cursor={Cursor}").json()
		Page = Response["data"]
		Cursor = Response["nextPageCursor"]

		Pages.append(Page)
		TotalBadges += len(Page)
	else:
		OS.system(ClearConsole)

		Display = AccInfo["displayName"]
		Name = AccInfo["name"]

		print(f"Badge Info for {Display} (@{Name}):\n")

		print(f"Total Badges: {str(TotalBadges)}")
		print(f"Total Pages: {str(len(Pages))}")

		break

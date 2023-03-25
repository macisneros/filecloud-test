from business import group_business

if __name__ == '__main__':
    groupedUsers = {
        "Accounting": [
            "Henderson Nakashima",
            "Biserka Wilkie",
            "Giltbert Thatcher",
            "Octavia Blanchard",
            "Dawid Morel"
        ],
        "Operations": [
            "Zülfikar Aafjes",
            "Vlasi Szilágyi",
            "Madelyn Donne",
            "Şule Zima",
            "Rehema Barr"
        ],
        "Engineering": [
            "Awee Murdoch",
            "Tsholofelo Boer",
            "Mari Winthrop"
        ],
        "Consultants": [
            "Dragoslav Echevarría",
            "Kaley Petrov"
        ]
    }

    group_business.addUsersToGroups(groupedUsers)
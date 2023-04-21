try:
            conn=mysql.connector.connect(host="loclahost",username="root",password="extra@191712",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("inset into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                       
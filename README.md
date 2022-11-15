
@Author Pham Thanh Phuc - B20DCCN512
@REFERENCES FROM ( ClearCode) and extends


I want to create a snake game with some simple function example for:
  1. create screen display with pause game, quit game and replay game.
  2. game will have 2 main object are snake and fruit. The fruit will appear at random in the screen and
    snake can move and eat them. When the snake eat fruit, the body of it will more longer
  3. All of snake and fruit have graphics and have sounds when snake eat fruit
  4. The game will have function count score
  5. 01/11/2022: update function"Level UP!" when snake has enough score 5,10,15 and it has sound for Level up!
 
 @Extension function will try to do:
  + Will speed up for snake when it qualifies
  + Create some map with impediment
  + Will snake eats enough fruit, it can change to next map
  + Have an item add score
  + Have three map level

 4/11 Done screen start game and function paused game
Game gồm 2 đối tượng chính là snake và fruit
Chúng ta sử dụng Vector2 để tạo ra các khối cho con rắn và fruit
Màn hình game gồm 2 trục x,y với 20 điểm tọa độ, mỗi tọa độ cách nhau 40px
Đầu tiên, tạo ra con rắn với 3 vector (5,10),(4,10),(3,10) cùng nằm trên một trục y = 10.
Một vector direction biểu thị di chuyển cho con rắn
+Tạo di chuyển cho con rắn :
	ban đầu, tạo một vector (0,0)là direction để biểu thị hướng đi chon con rắn, giá trị (0,0) tức là con rắn đang đứng yên 
	sử dụng các phím mũi tên để di chuyển thì vector direction sẽ :
		mũi tên đi lên thì direction(0,-1) tức là trục y sẽ giảm đi 1
		mũi tên xuống thì direction ( 0,1)
		mũi tên sang phải thì direction ( 1,0) tức trục x sẽ tăng thêm 1
		mũi tên sang trái thì direction ( -1,0)
	mỗi khi con rắn di chuyển, thì vector đầu tiên của body sẽ cộng với direction để biểu thị hướng di chuyển
+ Tạo đồ họa cho con rắn :
	việc tạo đồ họa cho con rắn gồm 3 phần là : tạo phần thân, phần đuôi và phần đầu
	*	về phần đầu, ta có vector relation_head = vector body[1] – vector body [0]
		nếu relation_head = ( 1,0) thì đầu con rắn sẽ hướng sang trái
		nếu relation_head = ( -1,0) thì đầu rắn hướng sang phải
		nếu relation_head = ( 0,-1) thì đầu rắn hướng xuống dưới
		nếu relation_head = ( 0,1) thì đầu rắn hướng lên trên
•	Phần đuôi:
có tail_ relation = vector body[-2] – vector body[-1], nếu:
	tail_relation = ( 1,0) , thì đuôi hướng sang trái
	tail_relation = ( -1,0), đuôi hướng sang phải
	tail_relation = ( 0,1), đuôi hướng lên
	tail_relation = ( 0,-1), đuôi hướng xuống
•	Phần thân:
 

sẽ có các graphics rẽ sang các hướng lần lượt là topleft, topright, bottomleft, bottomright
	
+Fruit : sẽ xuất hiện với vector có các x, y random

+Ktra va chạm:
nếu tọa độ x của đầu rắn không nằm trong khoảng từ 0 đến 20( size cửa sổ) thì sẽ dừng lại
hoặc nếu khối đầu của con rắn chạm vào phần thân sẽ dừng lại


version: "3.1"

nlu:
# # 00. General
# # 00.1 Lời chào
# - intent: greet
#   examples: |
#     - Xin chào
#     - Tôi cần tư vấn tuyển sinh đại học
#     - Cần tư vấn tuyển sinh
#     - hello
#     - hi
#     - Em đang muốn tìm hiểu về tuyển sinh đại học.
#     - Tìm hiểu về tuyển sinh đại học

# # 00.2 Lời chào tam biệt
# - intent: goodbye
#   examples: |
#     - Tạm biệt
#     - Hẹn gặp lại!
#     - Tạm biệt nhé!
#     - Bye
#     - Hẹn gặp lại lần sau
#     - Chào tạm biệt
#     - Bye bye
#     - Tạm biệt, cảm ơn bạn
#     - Hẹn gặp lại
#     - Chào và cảm ơn
#     - Tạm biệt, hy vọng được gặp lại
#     - Goodbye
#     - See you later
#     - Bye for now
#     - Tạm biệt và cảm ơn vì mọi thứ
#     - Tạm biệt, hẹn gặp lại sau
#     - Chào và tạm biệt
#     - Tạm biệt, mong được gặp lại
#     - Chúc bạn một ngày tốt lành
#     - Hẹn gặp lại trong tương lai
#     - Chào tạm biệt và cảm ơn
#     - Tạm biệt và chúc bạn may mắn
#     - Goodbye, hy vọng đã giúp được bạn
#     - See you next time
    

# # 00.3 Cảm ơn
# - intent: thank
#   examples: |
#     - Thank
#     - Cảm ơn bạn đã tư vấn
#     - Cảm ơn nhé
#     - Cảm ơn bạn nhiều
#     - Cảm ơn rất nhiều
#     - Thanks a lot
#     - Cảm ơn vì sự giúp đỡ
#     - Thank you
#     - Rất cảm ơn bạn
#     - Cảm ơn bạn vì tất cả
#     - Thanks for your help
#     - Cảm ơn vì đã tư vấn
#     - Cảm ơn bạn, rất hữu ích
#     - Thanks, bạn rất tốt
#     - Cảm ơn vì đã hỗ trợ
#     - Thank you for your assistance
#     - Cảm ơn bạn, rất cảm kích
#     - Thanks, bạn rất tận tâm
#     - Cảm ơn, bạn rất thông minh
#     - Thank you for your time
#     - Cảm ơn vì đã lắng nghe
#     - Thanks for everything
#     - Cảm ơn, bạn thật tuyệt vời
#     - Thank you, you've been a great help
    

# # 00.4 Hỏi giới tính
# - intent: gender
#   examples: |
#     - Nam
#     - Nữ
#     - Giới tính
#     - Giới tính của bạn là gì?
#     - Bạn là nam hay nữ?
#     - Bạn là nam hay nữ vậy?
#     - Bạn là nam hay nữ thế?
#     - Bạn là nam hay nữ nhỉ?
#     - Bạn thuộc giới tính nào?
#     - Bạn là giới tính gì?
#     - Giới tính của bạn là nam hay nữ?
#     - Bạn thuộc giới nào?
#     - Bạn xác định giới tính như thế nào?
#     - Bạn thuộc giới nào vậy?
#     - Bạn xác định giới tính ra sao?
#     - Bạn có phải là nam không?
#     - Bạn là nữ phải không?
#     - Giới tính của bạn là gì nhỉ?
#     - Bạn thuộc giới tính nào thế?
#     - Bạn thuộc giới nào nhỉ?
#     - Bạn có xác định giới tính không?
#     - Bạn thuộc giới nào, nam hay nữ?
#     - Bạn có giới tính không?
#     - Bạn là giới nào trong nam và nữ?
#     - Bạn thuộc giới tính nào, có thể chia sẻ không?
#     - Giới tính của bạn là gì, nam hay nữ?
#     - Bạn xác định giới tính như thế nào nhỉ?
#     - Bạn thuộc giới tính nào, bạn có thể nói không?
    

# # 00.5 Hỏi tuổi
# - intent: age
#   examples: |
#     - Ban sinh năm bao nhiêu?
#     - Bạn bao nhiêu tuổi?
#     - Bạn được tạo ra vào năm nào?
#     - Bạn được tạo ra khi nào?
#     - Tuổi của bạn là bao nhiêu?
#     - Bạn đã sống được bao lâu rồi?
#     - Bạn bao nhiêu tuổi rồi?
#     - Bạn có tuổi không?
#     - Tuổi tác của bạn là gì?
#     - Bạn được sinh ra từ bao giờ?
#     - Bạn tồn tại được bao lâu rồi?
#     - Tuổi của bạn là gì?
#     - Bạn đã tồn tại bao lâu?
#     - Bạn được tạo ra bao lâu rồi?
#     - Bạn có biết tuổi của mình không?
#     - Tuổi của bạn là bao nhiêu nhỉ?
#     - Bạn đã được mấy năm tuổi?
#     - Bạn có biết bạn bao nhiêu tuổi không?
#     - Bạn đã được sinh ra từ khi nào?
#     - Bạn bao nhiêu tuổi rồi nhỉ?
#     - Tuổi của bạn là gì vậy?
#     - Bạn đã sống được bao lâu nhỉ?
#     - Bạn đã tồn tại được bao nhiêu năm?
#     - Tuổi tác của bạn là bao nhiêu?
    

# # 00.6 Hỏi tên
# - intent: name
#   examples: |
#     - Tên bạn là gì?
#     - Bạn tên là gì?
#     - Bạn tên gì?
#     - Bạn tên là gì vậy?
#     - Bạn tên là gì nhỉ?
#     - Bạn tên là gì thế?
#     - Tên của bạn là gì?
#     - Bạn được đặt tên là gì?
#     - Tên của bạn là gì nhỉ?
#     - Tên của bạn là gì thế?
#     - Bạn có tên không?
#     - Tên của bạn là cái gì?
#     - Bạn được gọi là gì?
#     - Tên bạn là gì vậy?
#     - Bạn được biết đến với tên gì?
#     - Tên mà bạn có là gì?
#     - Bạn được đặt tên là gì nhỉ?
#     - Tên của bạn là gì, có thể chia sẻ không?
#     - Bạn có cái tên nào không?
#     - Tên bạn là cái gì nhỉ?
#     - Bạn được gọi là gì thế?
#     - Tên của bạn có ý nghĩa gì?
#     - Tên bạn nghĩa là gì?
#     - Tên của bạn có ý nghĩa là gì?
#     - Bạn có tên riêng không?
#     - Tên của bạn có gì đặc biệt không?
    

# # 00.7 Yêu cầu làm thơ
# - intent: make_poem
#   examples: |
#     - Làm thơ
#     - Làm thơ đi
#     - Làm thơ cho tôi
#     - Làm thơ cho tôi đi
#     - Làm thơ cho tôi được không?
#     - Làm thơ cho tôi được không nhỉ?
#     - Làm thơ cho tôi được không vậy?
#     - Hãy làm thơ giúp tôi
#     - Làm một bài thơ nhé
#     - Bạn có thể sáng tác thơ cho tôi?
#     - Hãy sáng tác một bài thơ
#     - Làm thơ về mùa xuân
#     - Làm thơ về tình yêu
#     - Sáng tác một bài thơ hay
#     - Hãy viết thơ cho tôi nghe
#     - Làm thơ về cuộc sống
#     - Làm thơ về thiên nhiên
#     - Bạn có thể làm thơ về tình bạn không?
#     - Làm thơ về một ngày mưa
    

# # 00.8 Hỏi người tạo ra
# - intent: who_created_you
#   examples: |
#     - Ai tạo ra bạn?
#     - Bạn được tạo ra bởi ai?
#     - Bạn được tạo ra bởi ai vậy?
#     - Bạn được tạo ra bởi ai nhỉ?
#     - Bạn được tạo ra bởi ai thế?
#     - Ai là người tạo ra bạn?
#     - Bạn được phát triển bởi ai?
#     - Người tạo ra bạn là ai nhỉ?
#     - Ai là người đã tạo nên bạn?
#     - Bạn được ai sáng tạo?
#     - Ai là cha mẹ của bạn?
#     - Ai là người chịu trách nhiệm tạo ra bạn?
#     - Bạn được tạo ra như thế nào?
#     - Ai là người đứng sau sự tồn tại của bạn?
#     - Người tạo ra bạn là ai thế?
#     - Bạn có biết ai tạo ra bạn không?
#     - Ai là người đã thiết kế bạn?
#     - Ai là người đã lập trình bạn?
#     - Bạn do ai tạo ra vậy?
#     - Người tạo ra bạn là ai, bạn có thể nói không?
#     - Bạn biết ai là người tạo ra mình không?
#     - Ai là người phát minh ra bạn?
#     - Bạn có biết người tạo ra bạn là ai không?
#     - Ai là người đã tạo nên trí tuệ của bạn?
#     - Bạn được tạo ra bởi ai, bạn có biết không?
    

# # 00.9 Hỏi chức năng
# - intent: what_can_you_do
#   examples: |
#     - Bạn có thể làm gì?
#     - Bạn có thể làm gì vậy?
#     - Bạn có thể làm gì nhỉ?
#     - Bạn có thể làm gì thế?
#     - Bạn có thể giúp gì cho tôi?
#     - Bạn có khả năng gì?
#     - Bạn có thể làm những gì?
#     - Bạn có thể giúp tôi với những gì?
#     - Bạn có chức năng gì?
#     - Bạn có thể làm những việc gì?
#     - Bạn có thể cung cấp thông tin gì?
#     - Bạn có thể hỗ trợ tôi như thế nào?
#     - Bạn có thể làm được những điều gì đặc biệt?
#     - Bạn có khả năng nào khác không?
#     - Bạn có thể giúp tôi tìm hiểu về gì?
#     - Bạn có thể thực hiện được những công việc gì?
#     - Bạn có thể tư vấn gì cho tôi?
#     - Bạn có thể làm được gì cho tôi biết?
#     - Bạn có thể giúp tôi về vấn đề gì?
#     - Bạn có thể làm gì để hỗ trợ tôi?
#     - Bạn có thể cung cấp những dịch vụ gì?
#     - Bạn có thể giúp tôi trong lĩnh vực nào?
#     - Bạn có thể làm gì để giúp đỡ?
#     - Bạn có khả năng tư vấn gì?
    

# # 00.10 Hỏi ngôn ngữ
# - intent: can_you_speak_english
#   examples: |
#     - Bạn có thể nói được tiếng anh không?
#     - Bạn có thể nói được tiếng anh không vậy?
#     - Bạn có thể nói được tiếng anh không nhỉ?
#     - Bạn có thể nói được tiếng anh không thế?
#     - Bạn có thể giao tiếp bằng tiếng Anh không?
#     - Bạn nói tiếng Anh được không?
#     - Bạn có khả năng nói tiếng Anh không?
#     - Bạn biết tiếng Anh phải không?
#     - Bạn có thể trả lời bằng tiếng Anh không?
#     - Bạn có thể hiểu tiếng Anh không?
#     - Tiếng Anh của bạn tốt không?
#     - Bạn có thể nói chuyện bằng tiếng Anh không?
#     - Bạn có thể sử dụng tiếng Anh không?
#     - Bạn có thể trò chuyện bằng tiếng Anh không?
#     - Tiếng Anh là ngôn ngữ bạn biết không?
#     - Bạn có khả năng giao tiếp tiếng Anh không?
#     - Bạn có thể phản hồi bằng tiếng Anh không?
#     - Bạn có thể nói tiếng Anh một cách lưu loát không?
#     - Bạn biết nói tiếng Anh đến mức nào?
#     - Bạn có thể hiểu và nói tiếng Anh không?
#     - Tiếng Anh là một trong những ngôn ngữ bạn nói không?
#     - Bạn có thể giúp tôi bằng tiếng Anh không?
#     - Bạn có thể trả lời câu hỏi bằng tiếng Anh không?
#     - Bạn có thể cung cấp thông tin bằng tiếng Anh không?
    

# # 00.11 Hỏi tên trường
# - intent: school_name
#   examples: |
#     - Tên trường của bạn là gì?
#     - Tên trường của bạn là gì vậy?
#     - Tên trường của bạn là gì nhỉ?
#     - Tên trường của bạn là gì thế?
#     - Trường bạn học là trường nào?
#     - Bạn học trường gì?
#     - Tên trường bạn theo học là gì?
#     - Bạn từ trường nào?
#     - Trường bạn đến từ đâu?
#     - Tên trường bạn học là gì vậy?
#     - Trường bạn học tên là gì?
#     - Bạn học trường nào thế?
#     - Trường bạn học có tên là gì?
#     - Bạn học tại trường nào?
#     - Bạn theo học trường nào?
#     - Tên trường bạn học là gì nhỉ?
#     - Bạn học trường nào, có thể nói không?
#     - Tên trường bạn đang học là gì?
#     - Bạn đang học tại trường nào?
#     - Bạn học tại trường gì vậy?
#     - Bạn đang theo học trường nào?
#     - Bạn học tại trường nào nhỉ?
#     - Tên trường bạn đang học là gì thế?
#     - Trường học của bạn tên là gì?
    

# # 00.12 Hỏi người yêu
# - intent: do_you_have_a_girlfriend
#   examples: |
#     - Bạn có người yêu chưa?
#     - Người yêu của bạn là ai?
#     - Bạn đã có bạn gái chưa?
#     - Bạn đang hẹn hò với ai?
#     - Bạn có mối quan hệ nào không?
#     - Bạn có đang trong một mối quan hệ không?
#     - Bạn có ai trong đời không?
#     - Bạn có bạn gái hay bạn trai không?
#     - Bạn đang yêu ai đó không?
#     - Bạn có người yêu chưa nhỉ?
#     - Bạn đã tìm được người yêu chưa?
#     - Bạn có mối quan hệ tình cảm nào không?
#     - Bạn có ai đó trong cuộc sống của bạn không?
#     - Bạn có người yêu hay chưa?
#     - Bạn có bạn gái hay chưa?
#     - Bạn đã có mối quan hệ nào chưa?
#     - Bạn có ai đó đặc biệt trong đời không?
#     - Bạn đã tìm thấy người yêu chưa?
#     - Bạn có người yêu nào không?
#     - Bạn đang yêu ai vậy?
#     - Bạn có người yêu không nhỉ?
#     - Bạn có ai đó ở bên không?
    

# # 00.13 Hỏi về thời tiết
# - intent: ask_weather
#   examples: |
#     - Hôm nay trời có lạnh không?
#     - Thời tiết ở đó đang ra sao?
#     - Hôm nay có mưa không?
#     - Trời đang nắng ở đó phải không?
#     - Hôm nay trời gió chăng?
#     - Dự báo thời tiết cho ngày mai thế nào?
#     - Trời có đang tuyết không?
#     - Hôm nay nhiệt độ bao nhiêu?
#     - Có cảm giác nóng lực nào không?
#     - Thời tiết hiện tại có phù hợp để đi chơi không?
#     - Cuối tuần này thời tiết thế nào?
#     - Thời tiết lúc này có khô ráo không?
#     - Trời có đang âm u không?
#     - Có sương mù vào buổi sáng không?
#     - Có khả năng bão không?
#     - Thời tiết có đang ảnh hưởng đến các hoạt động ngoài trời không?
#     - Hôm nay có phải là một ngày đẹp trời?
#     - Có cảnh báo thời tiết xấu không?
#     - Trời đang lạnh đến mức nào?
#     - Hôm nay có phải là ngày nắng đẹp không?
    

# # 00.14 Hỏi về giờ hiện tại
# - intent: ask_time
#   examples: |
#     - Bây giờ là mấy giờ?
#     - Hiện tại giờ địa phương là bao nhiêu?
#     - Mấy giờ rồi?
#     - Có phải bây giờ là giờ ăn trưa không?
#     - Giờ này cửa hàng vẫn mở cửa chứ?
#     - Hiện tại là giờ cao điểm không?
#     - Giờ này có quá muộn để gọi điện không?
#     - Có phải bây giờ là giờ nghỉ trưa không?
#     - Hiện tại là giờ làm việc hay giờ nghỉ?
#     - Giờ này trường học đã mở cửa chưa?
#     - Giờ này có phải là thời gian tốt để thăm viếng không?
#     - Có phải bây giờ là giờ tan tầm?
#     - Bây giờ là thời gian nào của ngày?
#     - Giờ này tiệm cafe vẫn mở không?
#     - Hiện tại có phải là giờ đúng để ăn tối?
#     - Giờ này có quá sớm để gọi điện không?
#     - Bây giờ là giờ gì theo giờ quốc tế?
#     - Giờ này có phải là lúc tốt nhất để đi chơi?
#     - Bây giờ là giờ vàng không?
#     - Giờ này trung tâm thương mại đã mở cửa chưa?
    

# # 00.15 Hỏi về ngày hiện tại
# - intent: ask_date
#   examples: |
#     - Hôm nay ngày bao nhiêu?
#     - Hôm nay là ngày gì theo lịch?
#     - Ngày hiện tại là ngày nào trong tuần?
#     - Hôm nay là ngày lễ gì không?
#     - Hôm nay có phải là cuối tuần không?
#     - Ngày này là kỷ niệm gì đặc biệt không?
#     - Ngày hôm nay có gì đặc biệt không?
#     - Hôm nay có phải ngày nghỉ lễ không?
#     - Có phải hôm nay là ngày đầu tiên của tháng không?
#     - Ngày hôm nay là ngày mấy của tháng?
#     - Hôm nay là ngày cuối cùng của tháng không?
#     - Hôm nay có phải là ngày quốc khánh không?
#     - Ngày hôm nay là ngày lễ tôn giáo không?
#     - Hôm nay có phải là ngày nghỉ quốc gia không?
#     - Ngày hôm nay có sự kiện gì nổi bật không?
#     - Hôm nay có phải là ngày sinh nhật của ai không?
#     - Hôm nay là ngày gì theo lịch âm?
#     - Ngày này trong lịch sử có gì đặc biệt không?
#     - Hôm nay là ngày khai giảng không?
#     - Có phải hôm nay là ngày kỷ niệm thành lập trường không?
    

# # 00.16 Hỏi về địa điểm
# - intent: ask_location
#   examples: |
#     - Bạn đang ở đâu?
#     - Vị trí hiện tại của bạn là gì?
#     - Bạn đang ở thành phố nào?
#     - Trường học này ở đâu?
#     - Cửa hàng này ở địa điểm nào?
#     - Tôi đang ở đâu trên bản đồ?
#     - Văn phòng này nằm ở khu vực nào?
#     - Trạm xe buýt gần nhất ở đâu?
#     - Bạn đang ở quận nào?
#     - Địa điểm này cách trung tâm bao xa?
#     - Đây là địa điểm du lịch nổi tiếng không?
#     - Bạn đang ở gần địa danh nào?
#     - Địa điểm này gần sân bay không?
#     - Địa điểm này thuộc tỉnh nào?
#     - Trường đại học này ở khu vực nào của thành phố?
#     - Địa điểm này gần ga tàu không?
#     - Địa điểm này có dễ tìm không?
#     - Nhà hàng này ở đâu trong thành phố?
#     - Bạn đang ở gần khu mua sắm nào?
#     - Công viên này nằm ở đâu trong thành phố?
    

# # 00.17 Yêu cầu trợ giúp
# - intent: request_help
#   examples: |
#     - Bạn có thể giúp tôi không?
#     - Tôi cần trợ giúp với bài tập này.
#     - Bạn có thể hỗ trợ tôi về thông tin tuyển sinh không?
#     - Làm thế nào để tôi có thể liên hệ với phòng hỗ trợ sinh viên?
#     - Tôi có thể nhận sự giúp đỡ ở đâu khi gặp vấn đề cá nhân?
#     - Tôi cần hướng dẫn về cách sử dụng thư viện.
#     - Bạn có thể chỉ cho tôi cách đăng ký các lớp học không?
#     - Tôi cần tư vấn về lựa chọn ngành học.
#     - Tôi có thể nhận trợ giúp về việc tìm chỗ ở không?
#     - Tôi gặp khó khăn trong việc hiểu một số quy định của trường.
#     - Bạn có thể giúp tôi tìm phòng y tế không?
#     - Tôi cần thông tin về học bổng.
#     - Bạn có thể giúp tôi với thủ tục visa không?
#     - Tôi cần trợ giúp trong việc lập kế hoạch học tập.
#     - Tôi có thể nhận sự hỗ trợ nào khi gặp vấn đề về tài chính?
#     - Làm thế nào để tôi có thể tham gia các hoạt động ngoại khoá?
#     - Tôi cần hỗ trợ trong việc tìm kiếm cơ hội thực tập.
#     - Tôi gặp vấn đề với hệ thống đăng ký môn học, bạn có thể giúp không?
#     - Bạn có thể hướng dẫn tôi cách sử dụng cổng thông tin sinh viên không?
#     - Tôi cần hỗ trợ trong việc quản lý thời gian học tập và làm việc.
    

# # 00.18 Hỏi về sở thích
# - intent: ask_hobbies
#   examples: |
#     - Bạn thích làm gì vào thời gian rảnh?
#     - Sở thích của bạn là gì?
#     - Bạn thường làm gì để giải trí?
#     - Bạn có sở thích đặc biệt nào không?
#     - Bạn thích đọc sách không?
#     - Bạn thích thể thao gì?
#     - Bạn có thích nghệ thuật không?
#     - Bạn thường làm gì vào cuối tuần?
#     - Bạn có thích đi du lịch không?
#     - Bạn thích nấu ăn không?
#     - Bạn có sở thích về âm nhạc không?
#     - Bạn có thích chơi nhạc cụ không?
#     - Bạn thích xem phim loại nào?
#     - Bạn có thích viết lách không?
#     - Bạn có sở thích sưu tầm gì không?
#     - Bạn thích hoạt động ngoại khóa nào ở trường?
#     - Bạn có thích chụp ảnh không?
#     - Bạn thích chơi game không?
#     - Bạn có thích vẽ không?
#     - Bạn có thích làm vườn không?
    

# # 00.19 Hỏi về sức khỏe
# - intent: ask_health
#   examples: |
#     - Bạn cảm thấy thế nào về sức khỏe của mình?
#     - Sức khỏe của bạn ổn không?
#     - Bạn có đang gặp vấn đề về sức khỏe không?
#     - Bạn đã ăn uống đủ chưa?
#     - Bạn có tập thể dục thường xuyên không?
#     - Bạn có đang mệt mỏi không?
#     - Bạn có gặp vấn đề gì với giấc ngủ không?
#     - Bạn có thường xuyên kiểm tra sức khỏe không?
#     - Bạn có cảm thấy căng thẳng không?
#     - Bạn có vấn đề gì về sức khỏe cần được quan tâm không?
#     - Bạn có uống đủ nước không?
#     - Bạn có bị dị ứng với thứ gì không?
#     - Bạn có đang tuân thủ chế độ ăn lành mạnh không?
#     - Bạn có thường xuyên bị đau đầu không?
#     - Bạn có bị cảm lạnh hay cảm cúm không?
#     - Bạn có thường xuyên cảm thấy mệt mỏi không?
#     - Bạn có bị bất kỳ chấn thương nào gần đây không?
#     - Bạn có vấn đề gì với mắt không?
#     - Bạn có bị đau lưng không?
#     - Bạn có thường xuyên kiểm tra thị lực không?
    

# # 00.20 Hỏi về tâm trạng
# - intent: ask_mood
#   examples: |
#     - Bạn cảm thấy thế nào hôm nay?
#     - Tâm trạng của bạn ra sao?
#     - Bạn có cảm thấy vui không?
#     - Hôm nay bạn cảm thấy buồn chán không?
#     - Bạn có cảm thấy căng thẳng hay lo lắng không?
#     - Bạn có hạnh phúc không?
#     - Bạn có cảm thấy thoải mái và yên tâm không?
#     - Bạn có phấn chấn không?
#     - Hôm nay bạn cảm thấy tự tin như thế nào?
#     - Bạn có cảm thấy mệt mỏi hay kiệt sức không?
#     - Bạn có cảm giác hứng khởi không?
#     - Bạn có đang cảm thấy lo âu hay bất an không?
#     - Bạn có cảm thấy hồi hộp không?
#     - Bạn có cảm thấy hài lòng với ngày hôm nay không?
#     - Bạn có cảm thấy bối rối hay lúng túng không?
#     - Bạn có cảm thấy tự tin vào bản thân không?
#     - Bạn có cảm thấy hài lòng với công việc hay học tập không?
#     - Bạn có cảm thấy bị áp lực không?
#     - Bạn có cảm thấy năng động và sáng tạo không?
#     - Bạn có cảm thấy hứng thú với những điều xung quanh không?
    

# # 00.21 Hỏi về kế hoạch cuối tuần
# - intent: ask_weekend_plans
#   examples: |
#     - Cuối tuần này bạn có kế hoạch gì không?
#     - Bạn dự định làm gì vào cuối tuần?
#     - Bạn có dự định đi đâu cuối tuần này không?
#     - Cuối tuần này bạn có gặp gỡ bạn bè không?
#     - Bạn có kế hoạch nghỉ ngơi hay giải trí gì không?
#     - Cuối tuần này bạn có tham gia sự kiện nào không?
#     - Bạn có dự định đi du lịch cuối tuần không?
#     - Bạn có dự định nấu món ăn gì đặc biệt không?
#     - Cuối tuần này bạn có kế hoạch xem phim hay đọc sách không?
#     - Bạn có dự định tham gia hoạt động thể thao cuối tuần không?
#     - Bạn có dự định thăm người thân không?
#     - Cuối tuần này bạn có làm việc nhà không?
#     - Bạn có dự định tổ chức hoặc tham dự tiệc không?
#     - Cuối tuần này bạn có dự định học cái gì mới không?
    

# # 00.22 Hỏi về công việc hoặc học tập
# - intent: ask_work_study
#   examples: |
#     - Bạn đang làm công việc gì hiện tại?
#     - Bạn học ngành gì ở trường?
#     - Bạn thích công việc của mình không?
#     - Bạn có hài lòng với ngành học của mình không?
#     - Bạn thường làm gì trong giờ làm việc?
#     - Bạn có kế hoạch học thêm gì sau khi tốt nghiệp không?
#     - Bạn làm việc trong lĩnh vực nào?
#     - Bạn đang theo đuổi mục tiêu học tập nào?
#     - Bạn thường gặp khó khăn gì trong công việc hoặc học tập?
#     - Bạn có dự định thay đổi công việc hoặc ngành học không?
#     - Công việc hiện tại có giúp bạn phát triển kỹ năng gì không?
#     - Bạn có tham gia hoạt động ngoại khóa nào tại trường không?
#     - Bạn thường làm việc ở đâu?
#     - Trường học của bạn có điểm nổi bật nào không?
#     - Bạn có kế hoạch nghề nghiệp sau khi tốt nghiệp không?
#     - Bạn có thích học nhóm hay học một mình không?
#     - Công việc hàng ngày của bạn bao gồm những gì?
#     - Bạn thích môi trường học tập hoặc làm việc hiện tại không?
#     - Bạn có dự định học lên cao hơn hoặc chuyển ngành không?
#     - Bạn thấy môn học hoặc dự án nào thú vị nhất trong quá trình học tập của mình?

- intent: buy_fashion
  examples: |
    - Tôi muốn mua cái [áo khoác](category_type)
    - Tôi muốn mua cái [quần jean](category_type)
    - Tôi muốn mua cái [áo polo](category_type).
    - Tôi muốn mua cái [áo](category_type) [sơ mi nam](category).
    - Tôi đang tìm kiếm chiếc [áo khoác](category_type) cho mùa đông.
    - Tôi muốn mua cái [áo thun](category) với hình in độc đáo.
    - Tôi cần một chiếc [áo len](category) để giữ ấm trong mùa lạnh.
    - Tôi muốn mua chiếc [áo](category_type) [hoodie thể thao](category).
    - Tôi đang tìm kiếm chiếc [áo khoác](category_type).
    - Tôi muốn mua chiếc [áo phông](category) với họa tiết hoa văn.
    - Tôi đang tìm kiếm chiếc [áo](category_type) [len mỏng](category) cho mùa xuân.
    - Tôi muốn mua chiếc [áo](category_type) [đen cổ tròn](category).
    - Tôi cần một chiếc [áo khoác](category_type) [da nam](category).s
    - Tôi muốn mua chiếc [áo thun](category) [trắng](color).
    - Tôi đang tìm kiếm chiếc [áo khoác](category_type) [kimono dễ thương](category).
    - Tôi muốn mua chiếc [áo](category_type) [đôi](category) cho cả gia đình.
    - Tôi đang tìm kiếm chiếc [áo](category_type) [thun dài tay](category) có in hình hoạt hình.
    - Tôi muốn mua cái [áo](category_type) [len cổ lọ](category).
    - Tôi cần một chiếc [áo](category_type) [polo màu pastel](category).
    - Tôi đang tìm kiếm chiếc [áo](category_type) [cardigan nam](category).
    - Tôi muốn mua cái [áo](category_type) [sơ mi nam](category) và [quần jean](category).
    - Tôi đang tìm kiếm chiếc [áo khoác](category_type) cho mùa đông và [quần](category_type) [kaki](category) đi kèm.
    - Tôi muốn mua cái [áo thun](category) với hình in độc đáo và [quần](category_type) [áo thun](category) thoải mái.
    - Tôi cần một chiếc [áo len](category) để giữ ấm trong mùa lạnh và [quần](category_type) [legging](category) điều chỉnh.
    - Tôi muốn mua chiếc [áo](category_type) [thể thao](category) và [quần](category_type) [jogger](category) phong cách.
    - Tôi đang tìm kiếm chiếc [áo khoác](category_type) [chống nước](category) và [quần](category_type) [chống nước](category) để hoàn thiện bộ trang phục.
    - Tôi muốn mua chiếc [áo](category_type) [phông](category) với họa tiết hoa văn và [quần](category_type) [váy maxi](category) điệu đà.
    - Tôi đang tìm kiếm chiếc [áo](category_type) [len mỏng](category) cho mùa xuân và [quần](category_type) [short](category) thoải mái.
    - Tôi muốn mua chiếc [áo](category_type) [đen cổ tròn](category) và [quần](category_type) [slacks](category) công sở.
    - Tìm giúp tôi một cái [áo](category_type) có giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"}
    - Tôi muối mua một cái áo [màu đỏ](color)
    - Cho tôi xin một chiếc [quần tây](category) [màu xanh](color) [size M](size) được không?
    - Tôi muốn mua một chiếc [quần tây](category) [màu xanh](color) với [size 29](size).
    - Bạn có [quần tây](category) nào [màu xanh](color) [size 29](size) không?
    - Tôi đang tìm kiếm [quần tây](category) [màu xanh](color) [kích thước 29](size) là lựa chọn của tôi.
    - Có thể tìm giúp tôi một chiếc [quần tây](category) [màu xanh](color) [size 29](size) được không?
    - Tôi quan tâm đến việc mua [quần tây](category) [màu xanh](color) [size 29](size) là yêu cầu của tôi.
    - Bạn có [quần tây](category) nào [màu xanh](color) [size 29](size) không?
    - Cho tôi xin một chiếc [quần tây](category) [màu xanh](color) [size 29](size) là ưu tiên của tôi.
    - Tôi muốn tìm một chiếc [quần tây](category) [màu xanh](color) có [size 29](size).
    - Có [quần tây](category) nào vừa vặn với [size 29](size) không?
    - Bạn có thể giới thiệu cho tôi một chiếc [quần tây](category) [màu xanh](color) [size 29](size) được không?
    - Tôi cần mua một chiếc [quần tây](category) [màu xanh](color) [size 29](size) là lựa chọn của tôi.
    - Bạn có [quần tây](category) nào [màu xanh](color) [size 29](size) không? Tôi đang cần mua ngay.
    - Cho tôi xin một chiếc [quần tây](category) [màu xanh](color) [size 29](size) là size phù hợp với tôi.
    - Có thể tìm giúp tôi một chiếc [quần tây](category) [màu xanh](color) [size 29](size) được không?
    - Tôi muốn tìm một chiếc [quần tây](category) [màu xanh](color) [kích thước 29](size) là yêu cầu của tôi.
    - Bạn có [quần tây](category) nào [màu xanh](color) [size 29](size) không? Tôi muốn mua ngay.
    - Cho tôi xin một chiếc [quần tây](category) [màu xanh](color) với [size 29](size).
    - Tôi cần mua một chiếc [quần tây](category) [màu xanh](color) [size 29](size) là yêu cầu của tôi.
    - Bạn có thể tìm giúp tôi một chiếc [quần tây](category) [màu xanh](color) có [size 29](size) không?
    - Bạn có [áo](category_type) nào có [kích thước M](size) không?
    - Tôi cần mua một chiếc [áo](category_type) [size M](size).
    - Cho tôi xin một chiếc [áo](category_type) với [kích thước M](size).
    - Tôi đang tìm kiếm [áo](category_type), [kích thước M](size) là lựa chọn của tôi.
    - Có thể tìm giúp tôi một chiếc [áo](category_type), [size M](size) được không?
    - Tôi quan tâm đến việc mua [áo](category_type) với [kích thước M](size).
    - Bạn có [áo](category_type) nào thuộc [size M](size) không?
    - Cho tôi xin một chiếc [áo](category_type), [size M](size) là ưu tiên của tôi.
    - Tôi muốn tìm một chiếc [áo](category_type) với [size M](size).
    - Có áo nào vừa vặn với [size M](size) không?
    - Bạn có thể tìm giúp tôi một chiếc [áo](category_type), [kích thước M](size) được không?
    - Tôi đang tìm kiếm [áo](category_type) với [kích thước M](size), bạn có thể gợi ý cho tôi không?
    - Tôi quan tâm đến việc mua một chiếc [áo](category_type) [size M](size).
    - Bạn có [áo](category_type) nào có [size M](size) không? Tôi đang cần mua một chiếc.
    - Cho tôi xin một chiếc [áo](category_type), [size M](size) là size phù hợp với tôi.
    - Có thể tìm giúp tôi chiếc [áo](category_type) với [kích thước M](size) được không?
    - Tôi muốn mua một chiếc [áo](category_type), [size M](size) là kích thước tôi đang tìm kiếm.
    - Bạn có [áo](category_type) nào có [size M](size) không? Tôi muốn mua ngay.
    - Cho tôi xin một chiếc [áo](category_type) vừa vặn với [size M](size).
    - Tôi cần mua một chiếc [áo](category_type), [size M](size) là yêu cầu của tôi.
    - Cho tôi xin một chiếc [áo len](category) có [màu xanh](color).
    - Tôi đang tìm kiếm [áo len](category)  [màu xanh](color) là sự lựa chọn của tôi.
    - Bạn có [áo len](category) nào [màu xanh](color) không?
    - Tôi muốn mua một chiếc [áo len](category)  [màu xanh](color) là yêu cầu của tôi.
    - Bạn có thể tìm giúp tôi một chiếc [áo len](category)  [màu xanh](color) được không?
    - Tôi quan tâm đến việc mua [áo len](category) [màu xanh](color).
    - Cho tôi xin một chiếc [áo len](category) với [màu xanh](color).
    - Bạn có [áo len](category) nào [màu xanh](color) không? Tôi đang cần mua một chiếc.
    - Tôi cần mua một chiếc [áo len](category)  [màu xanh](color) là lựa chọn của tôi.
    - Có thể tìm giúp tôi chiếc [áo len](category) với [màu xanh](color) được không?
    - Tôi muốn tìm một chiếc [áo len](category) [màu xanh](color).
    - Bạn có [áo len](category) nào có [màu xanh](color) không? Tôi muốn mua ngay.
    - Cho tôi xin một chiếc [áo len](category)  [màu xanh](color) là ưu tiên của tôi.
    - Tôi đang tìm kiếm [áo len](category)  bạn có thể gợi ý cho tôi chiếc áo [màu xanh](color) được không?
    - Tôi cần mua một chiếc [áo len](category) với [màu xanh](color).
    - Bạn có thể tìm giúp tôi chiếc [áo len](category) [màu xanh](color) được không?
    - Tôi muốn mua một chiếc [áo len](category) [màu xanh](color), bạn có gợi ý gì không?
    - Cho tôi xin một chiếc [áo len](category)  [màu xanh](color) là yêu cầu của tôi.
    - Tôi quan tâm đến việc mua một chiếc [áo len](category) [màu xanh](color).
    - Bạn có [áo len](category) nào [màu xanh](color) không? Tôi muốn mua ngay.
    - Bạn có cái [đầm](category_type) nào [màu xanh](color) không? Tôi muốn mua ngay.
    - Bạn có thể giúp tôi tìm một chiếc [áo phông](category) giá nằm trong khoảng từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} không?
    - Tôi cần tìm một chiếc [áo phông](category) với mức giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"}.
    - Cho tôi xin một [áo phông](category) giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} có được không?
    - Tôi quan tâm đến [áo phông](category) nhưng giá cần nằm trong khoảng từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"}.
    - Bạn có thể giới thiệu cho tôi một chiếc [áo phông](category) giá nằm trong khoảng từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} không?
    - Tôi muốn mua một chiếc [áo phông](category) với giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"}.
    - Cho tôi xin một chiếc [áo phông](category) có giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} được không?
    - Bạn có [áo phông](category) nào giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} không?
    - Tôi đang tìm [áo phông](category) giá nằm trong khoảng từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} có phải không?
    - Có thể giúp tôi tìm một chiếc [áo phông](category) giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} được không?
    - Tôi muốn mua [áo phông](category) với mức giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"}.
    - Cho tôi xin một [áo phông](category) giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} có được không?
    - Bạn có thể giúp tôi tìm chiếc [áo phông](category) giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} không?
    - Tôi cần một chiếc [áo phông](category) với giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"}.
    - Bạn có [áo phông](category) nào giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} không?
    - Tôi đang tìm [áo phông](category) giá cần phải từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"}.
    - Có thể giúp tôi tìm một chiếc [áo phông](category) giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} được không?
    - Tôi muốn mua [áo phông](category) với mức giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"}.
    - Cho tôi xin một [áo phông](category) giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} có được không?
    - Bạn có thể giúp tôi tìm chiếc [áo phông](category) giá từ [150]{"entity": "price", "role": "price_from"} đến [200]{"entity": "price", "role":"price_to"} không?


- lookup: category_type
  examples: |
    - áo
    - quần
    - váy
    - đầm

- synonym: đầm
  examples: |
    - sa rê
    - dress

- lookup: color
  examples: |
    - đỏ
    - xanh
    - vàng
    - đen
    - cam

- lookup: size
  examples: |
    - size S
    - size M
    - size L
    - size XL
    - size XXL
    - size Lớn
    - size Nhỏ
    - size 28
    - size 29
    - size 30
    - size 31
    - size 32
    - size 33
    - kích thước S
    - kích thước M
    - kích thước L
    - kích thước XL
    - kích thước XXL
    - kích thước lớn
    - kích thước nhỏ
    - kích thước 28
    - kích thước 29
    - kích thước 30
    - kích thước 31
    - kích thước 32
    - kích thước 33

- regex: price
  examples: |
    - \d+

- lookup: category
  examples: |
    - áo khoác
    - áo len
    - áo polo
    - Sơ mi nam
    - Khoác dạ
    - Thun
    - Len
    - Hoodie thể thao
    - Khoác chống nước
    - Phông
    - Len mỏng
    - Đen cổ tròn
    - Khoác da nam
    - Thun nền trắng
    - Khoác kimono dễ thương
    - Đôi
    - Thun dài tay
    - Len cổ lọ
    - Polo màu pastel
    - Khoác bomber
    - Cardigan nam
    - Hoodie màu xám
    - Khaki
    - Legging
    - Jogger
    - Chống nước
    - Váy maxi
    - Short
    - Slacks
    - mũ trùm đầu
    - mũ trùm
    - mũ trùm kín
    - mũ trùm kín đầu
    - mũ che đầu
    - mũ chụp đầu
    - mũ đội đầu
    - mũ đeo đầu
    - mũ lưỡi trai
    - mũ bucket
    - mũ fedora
    - mũ rộng vònh
    - áo lót
    - áo trong
    - áo ngực
    - áo nút ngực
    - áo nút vú
    - áo khoác len
    - áo len
    - áo len chui đầu
    - áo len có nón
    - áo len mũng
    - áo len dày
    - áo len dài tay
    - áo len ngắn tay
    - áo len cổ lọ
    - áo len cổ tim
    - áo len vằn thẳng
    - nỉ lót
    - nỉ lông
    - nỉ bông
    - nỉ mềm
    - nỉ ấm
    - nỉ dày
    - nỉ mịn
    - nỉ co giãn
    - nỉ không co giãn
    - áo hở vai
    - áo hai dây
    - áo tank top
    - áo bra top
    - áo crop top
    - áo halter top
    - áo chéo vai
    - áo ba lỗ
    - áo hở lưng
    - áo yếm
    - áo thun cổ lọ
    - áo thun cổ lọ tròn
    - áo thun cổ lọ thuyền
    - áo thun cổ lọ có cổ
    - áo thun cổ lọ tròn có cổ
    - áo thun cổ lọ thuyền có cổ
    - Áo nỉ
    - Áo có mũ trùm đầu
    - Áo len
    - Áo gió
    - Ao gió
    - áo cổ lọ
    - áo phông
    - áo thun có cổ
    - áo cánh
    - áo khoác ngoài
    - áo khoác lau bụi
    - áo khoác dã ngoại
    - áo khoác thám hiểm
    - áo khoác lót lông
    - áo khoác cách nhiệt
    - áo lạnh
    - áo khoác vải thô
    - áo khoác hải quân
    - áo khoác thủy thủ
    - áo khoác đồng hồ
    - áo mưa
    - áo choàng
    - áo len liền quần
    - áo len cao cổ
    - áo nỉ
    - áo sơ mi
    - áo vest
    - áo sơ mi không tay
    - áo sơ mi tay ngắn
    - áo cơ bắp
    - áo ngực thể thao
    - áo thun
    - áo đầu
    - áo khoác
    - áo len đan
    - quần áo ba lỗ
    - quần bó
    - quần yoga
    - quần thun
    - quần capri
    - quần xe đạp
    - quần bó sát chân
    - quần legging capris
    - quần legging
    - váy legging
    - áo len cổ cao
    - áo len cổ cuộn
    - áo len cổ polo
    - áo sơ mi cao cổ
    - áo cao cổ giả
    - áo cổ cuộn
    - áo cổ tròn
    - áo sơ mi henley
    - áo len cổ giả
    - quần cắt
    - quần ba phần tự
    - quần lót
    - quần thủy thủ
    - quần thuốc lá
    - quần ôm sát chân
    - quần kaki
    - quần dockers
    - quần yếm
    - quần vải thô
    - quần vải chéo
    - quần vải tơ sợi
    - quần dài
    - quần lửng
    - [quần tây](category) thường
    - quần ẩu
    - quần ông túm
    - quần áo đầy bản đạp
    - quần áo lót
    - quần váy
    - quần áo nửa váy
    - quần palazzo
    - quần culotte
    - quần short
    - quần short bermuda
    - quần jean cắt
    - quần nóng
    - quần ngắn
    - quần short ngắn
    - mũ rộng vành
    - quần jean
    - levis
    - quần jean xanh
    - quần jean đá
    - quần jean rách
    - quần jean đau khổ
    - quần jean ôm loe
    - quần jean mềm
    - quần jean bạn trai
    - quần jean co giãn
    - quần legging jean
    - quần co giãn
    - quần cầu lông
    - quần jegging
    - quần jegging gầy
    - quần cưỡi ngựa
    - quần jodhpuri
    - quần kỹ binh
    - quần short jodhpuri
    - quần short cưỡi ngựa
    - quần da bê
    - quần thể thao
    - quần chạy bộ
    - quần xích đạo
    - quần mỏ hôi
    - váy mã lai
    - váy quần
    - váy xà rông
    - váy dài
    - xà rông bãi biển
    - quần lót ống rộng
    - quần short tập gym
    - quần bơi
    - quần nỉ
    - quần tập thể dục
    - quần vừa vặn thoải mái
    - quần lưng thun
    - quần pyjama
    - quần short thường ngày
    - quần short thoải mái
    - đồ tắm
    - bikini
    - quần short jamaica
    - quần short lượt sóng
    - kimono
    - xà rông
    - màu tím
    - tím
    - mau trang
    - trang
    - mau vang
    - vang
    - mau cam
    - mau da cam
    - da cam
    - cam
    - mau hong
    - hong
    - mau xam
    - mau sam
    - sam
    - xam
    - mau xanh
    - mau da troi
    - xanh da troi
    - xanh
    - mau xanh la
    - xanh la cay
    - mau la cay
    - mau do
    - do
    - mau đo
    - đo
    - mau den
    - den
    - mau đen
    - đen
    - mau nau
    - nau
    - Áo choàng
    - áo len đan
    - Áo khoác lau bụi
    - Áo khoác dài
    - Áo khoác
    - váy
    - váy lót
    - đầm
    - yếm dài trẻ con
    - áo dài
    - quần quanh
    - váy maxi
    - váy màu

- intent: jacket
  examples: |
    - Áo khoác bán như thế nào
    - áo khoác dài bán ntn
    - tôi muốn xem áo khoác
    - Tôi muốn mua áo khoác
    - shop có bán áo khoác ko
    - có áo khoác nào mặc chống nắng ko
    - áo khoác mặc đi chơi có ko shop
    - cho xem áo khoác nha
    - có bán áo khoác ko
    - xem áo khoác
    - cho xem áo khoác
    - áo khoác có không?
- intent: sweater
  examples: |
    - có bán [áo len](category) không
    - tôi muốn mua áo len
    - cho xem [áo len](category) với
    - tôi muốn xem áo len
    - áo len shop có bán ko
    - xin mẫu [áo len](category) nha
    - mẫu áo len
    - có [áo len](category) ko shop
    - có [áo len](category) ko
    - shop có [áo len](category) ko
- intent: tee
  examples: |
    - xin mẫu áo phông
    - có bán áo phông không shop
    - muốn mua áo phông
    - mẫu áo ba lỗ
    - áo phông đẹp xin mẫu nha
    - có áo phông ko shop ơi
    - tôi muốn mua áo phông để đi chơi
    - áo phông shop có bán ko
    - mẫu áo phông đẹp tôi muốn xem
- intent: skirt
  examples: |
    - tôi mua váy lót
    - váy lót còn không shop
    - Chào bạn! Tôi đang tìm kiếm một chiếc váy dài cho buổi tiệc
    - cần tim mua váy đi đám cưới
    - cần váy đẹp
    - muốn mua váy
    - shop còn váy nào đẹp ko
    - shop có bán váy ko
- intent: shorts
  examples: |
    - tôi muốn mua quần short
    - mua quần short
    - quần short
    - có quần short không shop
    - quần short bán sao
    - có quần short không
    - quần short shop có bán ko
    - tôi muốn xem quần short
    - mẫu quần short shop có ko
- intent: leggings
  examples: |
    - có quần bó không
    - mặc quần thun thoải mái
    - tôi muốn mua quần bó
    - Quần bó sát chân
    - quần bó
    - quần bó mặc đẹp
    - tôi muốn mua quần thun
    - có quần thun ko
    - quần thun
    - quần thun shop có ko
    - shop có quần thun ko
    - muốn xem quần thun
    - quần bó shop có bán ko
    - quần bó shop còn hàng ko
- intent: jeans
  examples: |
    - Quần jean
    - tôi muốn mua Quần jean
    - có Quần jean đẹp ko
    - Quần jean có bán ko shop
    - mua Quần jean
    - có Quần jean ko
    - cho hỏi có bán Quần jean ko
    - quần jean shop còn hàng ko
    - muốn xem quần jean
    - cho xem quần jean với
    - shop có bán quần jean ko
    - gửi mẫu quần jean cho tôi xem
    - cho xem quần jean
    - xem quần jean
- intent: size_skirt
  examples: |
    - Váy thì có loại size nào shop?
    - váy này shop có mấy size
    - shop có size loại váy này ko
    - Váy này có mấy size
    - size váy này có loại nào lớn ko
    - Váy này có size nhỏ không
    - size váy nào thì người gầy mặc đẹp
- intent: color_skirt
  examples: |
    - Váy có mấy loại màu shop
    - cho xem các màu của váy
    - váy có mấy màu
    - váy này có mấy nào shop
    - da trắng mặc váy màu gì đẹp
    - người gầy thì mặc váy màu nào hợp
    - người bự con mặc váy màu nào ok nhất
    - shop có váy màu nào
    - váy có những màu nào há
    - váy thì shop có những màu nào
- intent: size_l_jacket
  examples: |
    - áo khoác có size L ko shop
    - Shop có bán áo khoác size L ko
    - có áo khoác size L ko
    - cho xem áo khoác size L
    - muốn xem áo khoác size L
    - áo khoác size L
    - bao nhiêu kg thì mặc áo khoác size L
    - cao bao nhiêu thì mặc áo khoác size L
    - nam nữ có mặc chung áo khoác size L được ko
- intent: size_jacket
  examples: |
    - shop có bao nhiêu size áo khoác
    - có bao nhiêu size áo khoác
    - áo khoác có size lớn ko
    - có size áo khoác nhỏ ko
    - áo khoác size nhỏ
    - áo khoác size lớn
    - tôi muốn xem size áo khoác
    - cho tôi xem các size áo khoác
    - nặng 50kg mặc áo khoác size nào shop
    - shop gửi các size áo khoác cho mình xem nhé
- intent: size_xl_jacket
  examples: |
    - áo khoác size XL
    - xem áo khoác XL
    - Áo khoác XL
    - cho xem áo khoác size XL
    - muốn xem áo khoác XL
    - to con mặc áo khoác XL được ko
- intent: size_xl_l_jacket
  examples: |
    - cho xem áo khoác size L và XL luôn nha
    - áo khoác L và XL
    - cho xem cả 2 size L và XL của áo khoác nha
    - cho tôi xem áo khoác size L và XL
    - xem áo khoác size L và XL
- intent: color_grey_skirt
  examples: |
    - cho xem váy màu xám nha shop
    - tôi muốn xem váy màu xám
    - váy màu xám nha
    - Shop có bán váy màu xám ko ?
    - váy màu xám shop có ko?
    - xem váy màu xám
    - cho xem váy màu xám
- intent: color_green_skirt
  examples: |
    - cho xem váy [màu xanh](color) nhé
    - shop còn váy [màu xanh](color) ko
    - muốn xem váy [màu xanh](color)
    - váy [màu xanh](color) nha
    - Váy [màu xanh](color)
    - cho tôi xem váy [màu xanh](color)
    - tôi xem váy [màu xanh](color)
    - xem váy [màu xanh](color)
    - gửi tôi xem váy [màu xanh](color)
- intent: greeting
  examples: |
    - tôi muốn mua sản phẩm
    - có ai ko
    - hi shop
    - cho tôi hỏi
    - bạn ơi
    - hello
    - hi
    - hey
    - có ai ở đây không?
    - chào shop
    - Có ai ở đây không nhỉ
    - alo
    - hú hú
    - cho hỏi
    - shop ơi
    - tôi muốn mua
    - alo alo
    - chào
    - hello shop
    - tôi có câu hỏi
    - muốn hỏi chút
- intent: color_grey_green_skirt
  examples: |
    - cho xem váy [màu xanh](color) và màu xám luôn nha
    - shop có bán váy [màu xanh](color) và màu xám ko
    - xem váy [màu xanh](color) và màu xám
    - tôi muốn xem váy [màu xanh](color) và màu xám
    - muốn xem váy màu xám và [màu xanh](color) nha
- intent: size_s_skirt
  examples: |
    - cho xem váy size S nha shop
    - muốn xem váy size S
    - shop có váy size S ko
    - váy size S
    - xem váy size S
    - cho tôi xem váy size S nha
- intent: size_m_skirt
  examples: |
    - cho xem váy size M nha
    - shop có váy size M ko
    - xem váy size M
    - váy size M
    - muốn xem váy size M
    - cho tôi xem váy size M
    - shop còn váy size M ko
    - tôi muốn xem váy size M
- intent: thanks
  examples: |
    - cảm ơn
    - cảm ơn nha
    - Thank you
    - Thank
    - Tuyệt vời lắm
    - Cảm ơn bạn rất nhiều
    - Oke lắm
    - điều này tuyệt nhất
    - Tạm biệt
    - bye shop
    - bye
    - cảm ơn hen
    - Cảm ơn shop nha
    - bay bay
    - bye bye
    - cảm ơn Shop
    - mơn nhe
    - bi bi
    - by by
    - bay
    - chào tạm biệt
    - cảm ơn shop rất nhiều
    - hẹn gặp lại shop
- intent: goodbye
  examples: |
    - cảm ơn shop
    - tạm biệt
    - không mua nữa
    - không mua
    - baibai
    - baybay
    - hẹn bửa khác
    - goodbye
    - bb
    - dịp khác nha
    - vậy thôi nhé
    - bay
    - bai
    - bửa sau quay lại
    - bai nhé
    - bai shop
- intent: size_m_s_skirt
  examples: |
    - muốn xem cả 2 size M và size S
    - shop có váy size S và size M ko
    - váy size S và M
    - xem váy size S và M
    - muốn xem váy size S và M nha
    - tôi xem váy size S và M
    - người nhỏ con thì mặc váy size S và M ok ko shop hé

import requests
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


#--tạo navigation ---
selected = option_menu(
    menu_title=None,
    options=["Giới Thiệu","Dự Án","Liên Hệ"],
    icons =["house","book","envelope"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal")


#-- tạo sidebar-----
st.sidebar.header("Đánh gía website của Quyền")
st.sidebar.write("##")
st.sidebar.date_input("Ngày bạn ghé thăm web của tớ?")
st.sidebar.text_input("Tên của bạn?","Viết tên của bạn ở đây")
st.sidebar.radio("Bạn quen Quyền qua đâu?",["Mạng xã hội","Học Chung","Bạn bè giới thiệu"])
st.sidebar.slider("Thang điểm bạn cho Quyền?",0,100)
st.sidebar.selectbox("Điều cần cải thiện nhất?",["Màu sắc","Bố Cục","Nội dung","Khác"])
st.sidebar.multiselect("Bạn thấy ấn tượng nhất?",["Khả năng của Quyền","Màu sắc","Nội dung","Cách trình bày"])
st.sidebar.text_area("Góp ý chuyên sâu của bạn")
st.sidebar.button("Gửi góp ý cho Quyền")
st.sidebar.success("Cảm ơn b nhiều nhé, mãi iu <3")

if selected == "Giới Thiệu":



    # page1---------------------------------------------------------------------------------------------------------------------------------------
    #==============================================================================================================================================
    #-------header------
    with st.container():
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.title("Trần Mạnh Quyền")
            st.write("Xin chào mọi người, tớ là Quyền, năm nay tớ 24 tuổi."
                     " Hiện tớ đã tốt nghiệp khoa Du Lịch trường Đại Học Mở Hà Nội."
                     " Sở thích của tớ là chơi nhạc cụ và học hỏi thêm những thứ mới."
                     " Và đó là lý do tớ có website này. "
                     " Tớ muốn có 1 website do tớ code hoàn toàn theo ý muốn và đây là sản phẩm"
                     " đầu tay của tớ, hi vọng các bạn sẽ thích hehe <3")

            st.write("[Thêm thông tin về tớ >](https://www.facebook.com/)")



    #----nội dung tiếp theo -----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns((3,2))
        with left_column:
            st.header("Ưu - nhược điểm của tớ")
            st.subheader("Ưu điểm")
            st.write("""
                     - Tớ có thể sử dụng tiếng Anh giao tiếp ở mức độ khá do có 2 năm kinh nghiệm dẫn
                      tour cho khách nước ngoài
                     - Tớ biết chơi nhạc cụ phổ biến như : Guitar, sáo và 1 chút piano
                     - Tớ nền tảng excel và tin hoc văn phòng nói chung khá tốt
                     - 1 chút kiến thức về lập trình VBA và Python giúp tớ tự động hóa được
                     công việc của bản thân và làm thêm nhiều điều thú vị""")
            st.subheader("Nhược điểm")
            st.write("""
                     - Tớ hay bị overthinking hehe"
                     - Tớ dễ thay đổi môi trường sống, công việc do tớ cảm thấy dễ nhàm chán
                     - Đôi lúc tớ cũng không có giao tiếp khéo léo cho lắm
                     - Tớ mải chơi và rất hay chơi game "
                     - Và hàng tá nhược điểm khác nữa về tớ.....""")
        with right_column:
            st.write("###")
            st.write("###")
            st.write("###")
            st.write("###")
            st.write("###")
            uunhuoc = Image.open("C:\\Users\\ADMIN\\Desktop\\image\\uunhuoc.png")
            uunhuoc = uunhuoc.resize((500, 300))
            st.image(uunhuoc)


#-------page 2 ------------------------------------------------------------------------------------------------------------------
#===================================================================================================================================
tourguide = Image.open("C:\\Users\\ADMIN\\Desktop\\image\\tourguide.png")
vba = Image.open("C:\\Users\\ADMIN\\Desktop\\image\\vba.png")
python = Image.open("C:\\Users\\ADMIN\\Desktop\\image\\python.png")
guitar = Image.open("C:\\Users\\ADMIN\\Desktop\\image\\guitar.png")

vba = vba.resize((500, 250))
tourguide = tourguide.resize((500, 300))
python = python.resize((500, 250))
guitar = guitar.resize((500, 300))


if selected == "Dự Án":
    #-----vba project--
    with st.container():
        st.header("Những dự án nhỏ tớ đã làm")
        left_column,right_column = st.columns((2,2))
        with right_column:
            st.subheader("VBA project")
            st.write("Lần đầu tiên tớ tiếp xúc với ngôn ngữ lập trình"
                     " vba là vào năm 2022. Sau khoảng 1 năm mày mò tự học"
                     "trên mạng thì tớ cảm thấy khá là thích môn này. Hầu hết"
                     "các công việc văn phòng chỉ cần có vba là có thể tiết kiệm"
                     "thời gian rất nhiều. Tớ đã từng giảm thời gian làm báo cáo"
                     "từ 4 tiếng -> chỉ còn 4 giây.")

            st.markdown("[Tham khảo khóa vba tớ đã học>]()")
        with left_column:
            st.image(vba)
        st.write("##")

    #----python project
    with st.container():

        left_column, right_column = st.columns((2, 2))
        with right_column:
            st.subheader("Python project")
            st.write("So với VBA thì Python xa lạ hơn với những bạn không chuyên"
                     " về lập trình như tớ. Python là một ngôn ngữ mạnh mẽ với cú"
                     "pháp đơn giản , dễ hiểu, dễ học. Python đã giúp tớ dễ dàng hơn"
                     " trong việc tự động hóa công việd văn phòng với nhiều tiện"
                     "ích vượt xa vba. Và dự án gần đây nhất tớ làm chính là website"
                     "này ")

            st.markdown("[Đọc bài viết này hiểu thêm về python>]()")
        with left_column:
            st.image(python)
        st.write("##")

    #-------tourguide-------------------------
    with st.container():

        left_column, right_column = st.columns((2, 2))
        with right_column:
            st.subheader("Tourguide")
            st.write("Chuyên ngành của tớ cũng là hướng dẫn viên luôn ( tourguide)."
                     "Tớ may mắn có được khoảng 2 năm kinh nghiệm dẫn tour, trong đó"
                     "có hơn 1 năm là tourguide tình nguyện cho câu lạc bộ dẫn tour"
                     "cho người nước ngoài của các bạn sinh viên Hanoi Ebuddies."
                     "Sau đó tớ xin làm chính thức cho công ty dẫn tour xe máy Hanoi Backstreet Tour."
                     "Tớ nghĩ đây là khoảng thời gian thú vị và thử thách nhất cho tới thời điểm"
                     "hiện tại")

            st.markdown("[Xem thêm về công ty của tớ>]()")
        with left_column:
            st.image(tourguide)
        st.write("##")

# -------guitar-----------
    with st.container():
        left_column, right_column = st.columns((2, 2))
        with right_column:
            st.subheader("Guitar")
            st.write("Thực tế tớ không nghĩ tớ sẽ cho nó vào thành 1 project thực sự"
                     "Nhưng tớ vẫn thêm vào vì đơn giản âm nhạc với tớ rất quan trọng"
                     "và là liều thuốc chữa lành cho tớ những lúc chán nản mệt mỏi."
                     "Bên trái là ảnh tớ biểu diễn cho đoàn thanh niên của xã "
                     "Tiền An- Quảng Yên- Quảng Ninh"
                     )

            st.markdown("[Thêm video tớ hay đánh>]()")
        with left_column:
            st.image(guitar)





#------------page3----------------------------------------------------------------------------------------------------------------
if selected == "Liên Hệ":
    st.header("Cách liên hệ với Quyền")
    st.write("##")
    left_column,right_column = st.columns((2,2))
    with left_column:
        st.subheader("Mạng xã hội")
        st.write("---")
        st.markdown("##### Facebook")
        st.markdown("###### Facebook Quyền thường online vào khoảng từ 17h-23h,"
                    "thời gian hành chính vui lòng không liên hệ qua facebook ")
        st.markdown("[Link Facebook](https://www.facebook.com/)")
        st.write("---")

        st.subheader("Email")
        st.markdown("###### Thường thì Quyền sẽ check email vào thứ 2 đầu tuần và"
                    "sẽ phản hồi lại trong ngày. Đối với các vấn đề liên quan tới"
                    "công việc Quyền khuyến khích mọi nguời liên hệ qua hình thức"
                    "này")
        st.markdown("###### Địa chỉ mail: tranmanhquyenqn@gnail.com")

        st.write("---")
        st.subheader("Số điện thoại")
        st.markdown("###### Sử dụng khi liên lạc bằng cả 2 cách trên nhưng không được")
        st.markdown("###### Số điện thoại : 0394 372 820")


-- ----------------------
-- Create Channel table
-- ----------------------
CREATE TABLE Channel
(
  id_channel      CHAR(15)  NOT NULL,
  channel_title   CHAR(100)  NOT NULL
);

-- ----------------------
-- Create Video table
-- ----------------------
CREATE TABLE Video
(
  video_id       CHAR(15)  NOT NULL,
  id_channel     CHAR(15)  NOT NULL,
  video_title    CHAR(200) NOT NULL,
  category_id    INTEGER   NOT NULL,
  publish_time   DATE      NOT NULL  
);

-- ----------------------
-- Create Video_Rating table
-- ----------------------
CREATE TABLE Video_Rating
(
  video_id       CHAR(15)       NOT NULL,
  act_date       DATE           NOT NULL,
  likes          DECIMAL(30, 5) NOT NULL,
  dislikes       DECIMAL(30, 5) NOT NULL,
  v_views        DECIMAL(30, 5) NOT NULL,
  comments       DECIMAL(30, 5) NOT NULL 
);

-- ----------------------
-- Create Category table
-- ----------------------
CREATE TABLE Category
(
  category_id    INTEGER        NOT NULL,
  name_category  CHAR(50)       NOT NULL 
);

ALTER TABLE channel ADD PRIMARY KEY (id_channel);
ALTER TABLE video ADD PRIMARY KEY (video_id);
ALTER TABLE video_Rating ADD PRIMARY KEY (video_id);
ALTER TABLE category ADD PRIMARY KEY (category_id);

ALTER TABLE video ADD CONSTRAINT FK_Video_Channel FOREIGN KEY (id_channel) REFERENCES channel (id_channel);
ALTER TABLE video ADD CONSTRAINT FK_Video_Category FOREIGN KEY (category_id) REFERENCES category (category_id);
ALTER TABLE video_rating ADD CONSTRAINT FK_Video_Rating FOREIGN KEY (video_id) REFERENCES video (video_id);
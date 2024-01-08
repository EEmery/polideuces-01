import cv2 as cv


class DisplayWindow:
    def __init__(self, window_name=None, headers=None, footers=None):
        self.window_name = window_name
        self.vc = None
        self.esc_key = 27
        cv.namedWindow(window_name)

        self.headers = headers
        self.footers = footers

        self.text_font = cv.FONT_HERSHEY_PLAIN
        self.text_scale = 1
        self.text_color = (255, 255, 255)
        self.text_thickness = 1
        self.text_line_type = cv.LINE_AA
        self.text_left_padding = 10
        self.text_top_padding = 10
        self.text_left_margin = 0
        self.text_top_margin = 0

        self.rect_color = (0, 0, 0)
        self.rect_thickness = -1
        self.rect_line_type = cv.LINE_AA

        self.frame_top_margin = 10
        self.frame_left_margin = 10

    def init_webcam(self):
        self.vc = cv.VideoCapture(0)

    async def close(self):
        if self.vc is not None:
            self.vc.release()
        cv.destroyWindow(self.window_name)

    def get_webcam_frame(self):
        if self.vc is not None:
            rval, frame = self.vc.read()
            return rval, frame
        else:
            raise Exception("You must initialize the webcam first with .init_webcam()")

    def update_frame(self, frame, info={}, headers=None, footers=None):
        key = cv.waitKey(20)

        frame = self._draw_on_frame(frame, info, headers, footers)

        cv.imshow(self.window_name, frame)

        return key == self.esc_key

    def _draw_on_frame(self, frame, info, headers, footers):
        info_texts = [f"{k}: {v}" for k, v in info.items()]
        header_texts = headers or self.headers or []
        footer_texts = footers or self.footers or []
        all_texts = header_texts + info_texts + footer_texts

        max_width = max(
            [
                cv.getTextSize(text, self.text_font, self.text_scale, self.text_thickness)[0][0]
                for text in all_texts
            ]
        )

        for i, text in enumerate(all_texts):
            (text_width, text_height), _ = cv.getTextSize(
                text, self.text_font, self.text_scale, self.text_thickness
            )

            text_x = self.frame_left_margin + self.text_left_margin + self.text_left_padding
            text_y = self.frame_top_margin + (
                self.text_top_margin + self.text_top_padding + text_height
            ) * (i + 1)

            rect_x1 = text_x - self.text_left_padding
            rect_y1 = text_y - text_height - self.text_top_padding
            rect_x2 = text_x + max_width + self.text_left_padding
            rect_y2 = text_y + self.text_top_padding

            cv.rectangle(
                frame,
                (rect_x1, rect_y1),
                (rect_x2, rect_y2),
                self.rect_color,
                self.rect_thickness,
                self.rect_line_type,
            )
            cv.putText(
                frame,
                text,
                (text_x, text_y),
                self.text_font,
                self.text_scale,
                self.text_color,
                self.text_thickness,
                self.text_line_type,
            )

        return frame

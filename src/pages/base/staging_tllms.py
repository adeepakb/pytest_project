from abc import ABC, abstractmethod


class StagingtllmsBase(ABC):
    @abstractmethod
    def login_to_staging(self):
        raise NotImplementedError()

    @abstractmethod
    def get_tutor_url(self):
        raise NotImplementedError()

    @abstractmethod
    def reset_session(self):
        raise NotImplementedError()

    @abstractmethod
    def get_mobile_and_ccode(self):
        raise NotImplementedError()

    @abstractmethod
    def get_otp(self):
        raise NotImplementedError()

    @abstractmethod
    def wait_for_locator_webdriver(self):
        raise NotImplementedError()

    @abstractmethod
    def wait_for_clickable_element_webdriver(self):
        raise NotImplementedError()

    @abstractmethod
    def wait_for_element_not_present_webdriver(self):
        raise NotImplementedError()

    @abstractmethod
    def select_course(self):
        raise NotImplementedError()

    @abstractmethod
    def select_topic_and_update_teaching_material(self):
        raise NotImplementedError()

    @abstractmethod
    def login_to_cms_staging(self):
        raise NotImplementedError()

    @abstractmethod
    def update_teaching_material(self):
        raise NotImplementedError()

    @abstractmethod
    def is_session_present_today(self):
        raise NotImplementedError()

    @abstractmethod
    def is_teaching_material_tagged(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_teaching_material_link(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_teaching_material_page(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_add_material_button(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_teaching_material_popup(self):
        raise NotImplementedError()

    @abstractmethod
    def click_outside_upload_teaching_material_popup(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_teaching_material_popup_is_closed(self):
        raise NotImplementedError()

    @abstractmethod
    def close_driver(self):
        raise NotImplementedError()

    @abstractmethod
    def close_upload_teaching_material_dialog(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_teaching_material_page_pagination(self):
        raise NotImplementedError()

    @abstractmethod
    def set_material_name(self):
        raise NotImplementedError()

    @abstractmethod
    def choose_pdf_file(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_file_other_than_pdf_cannot_be_selected(self):
        raise NotImplementedError()

    @abstractmethod
    def click_on_submit_teaching_material_page(self):
        raise NotImplementedError()

    @abstractmethod
    def is_uploaded_file_present(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_page_num_is_highlighted(self):
        raise NotImplementedError()

    @abstractmethod
    def add_role_to_user(self):
        raise NotImplementedError()

    @abstractmethod
    def is_role_added(self):
        raise NotImplementedError()

    @abstractmethod
    def set_assessment_start_date(self):
        raise NotImplementedError()

    @abstractmethod
    def set_assessment_end_date(self):
        raise NotImplementedError()

    @abstractmethod
    def get_assessment_available_until_date(self):
        raise NotImplementedError()

    @abstractmethod
    def attach_requisite(self):
        raise NotImplementedError()

    @abstractmethod
    def saved_session(self):
        raise NotImplementedError()

    @abstractmethod
    def session_relaunch(self):
        raise NotImplementedError()

    @abstractmethod
    def get_premium_id(self):
        raise NotImplementedError()

    @abstractmethod
    def _pid(self):
        raise NotImplementedError()

    @abstractmethod
    def working_day(self):
        raise NotImplementedError()

    @abstractmethod
    def otm_home_screen(self):
        raise NotImplementedError()

    @abstractmethod
    def get_session_completed_up_next_date(self):
        raise NotImplementedError()

    @abstractmethod
    def date_check(self):
        raise NotImplementedError()

    @abstractmethod
    def _req_grp_name(self):
        raise NotImplementedError()

    @abstractmethod
    def _requisite_group(self):
        raise NotImplementedError()

    @abstractmethod
    def _session_user_wise(self):
        raise NotImplementedError()

    @abstractmethod
    def attach_requisite_group(self):
        raise NotImplementedError()

    @abstractmethod
    def destroy_tabs(self):
        raise NotImplementedError()

    @abstractmethod
    def _session_url(self):
        raise NotImplementedError()

    @abstractmethod
    def end_ongoing_session(self):
        raise NotImplementedError()

    @abstractmethod
    def detach_requisite_attachment(self):
        raise NotImplementedError()

    @abstractmethod
    def is_otm_session_activity(self):
        raise NotImplementedError()

    @abstractmethod
    def get_otm_first_session_detail(self):
        raise NotImplementedError()

    @abstractmethod
    def reset_session_one_to_mega(self):
        raise NotImplementedError()

    @abstractmethod
    def topic_id_row(self):
        raise NotImplementedError()

    @abstractmethod
    def _license_key(self):
        raise NotImplementedError()

    @abstractmethod
    def _video_url(self):
        raise NotImplementedError()

    @abstractmethod
    def _write_key_license(self):
        raise NotImplementedError()

    @abstractmethod
    def _attachment_write(self):
        raise NotImplementedError()

    @abstractmethod
    def attach_session_video(self):
        raise NotImplementedError()

    @abstractmethod
    def requisite_assessment(self):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def booking_time():
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_available_slots():
        raise NotImplementedError()

    @abstractmethod
    def _add_slot(self):
        raise NotImplementedError()

    @abstractmethod
    def verify_and_add_slot(self):
        raise NotImplementedError()

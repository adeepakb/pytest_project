from abc import ABC, abstractmethod


class ClassNotesBase(ABC):

    @abstractmethod
    def is_classnote_icon_present(self):
        raise NotImplemented()

    @abstractmethod
    def is_download_icon_present(self):
        raise NotImplemented()

    @abstractmethod
    def tap_on_first_session_card(self):
        raise NotImplemented()

    @abstractmethod
    def is_requisite_list(self):
        raise NotImplemented()

    @abstractmethod
    def click_on_download(self):
        raise NotImplemented()

    @abstractmethod
    def classnote_processing(self):
        raise NotImplemented()

    @abstractmethod
    def is_assets_in_pdf_format(self):
        raise NotImplemented()

    @abstractmethod
    def all_tagged_resource_types(self):
        raise NotImplemented()

    @abstractmethod
    def verify_classnotes_present_to_download(self):
        raise NotImplemented()

    @abstractmethod
    def verify_forward_icon_present(self):
        raise NotImplemented()

    @abstractmethod
    def verify_or_select_pdf_viewer(self):
        raise NotImplemented()

    @abstractmethod
    def verify_pdf_viewer_options(self):
        raise NotImplemented()

    @abstractmethod
    def tap_classnotes_forward_icon_and_verify(self):
        raise NotImplemented()

    @abstractmethod
    def click_on_pdf_download_option(self):
        raise NotImplemented()

    @abstractmethod
    def verify_share_file_options(self):
        raise NotImplemented()

    @abstractmethod
    def verify_no_pdf_viewer_message(self):
        raise NotImplemented()

    @abstractmethod
    def login_to_cms_staging(self):
        raise NotImplemented()

    @abstractmethod
    def upload_class_note_morethan_15mb(self):
        raise NotImplemented()

    @abstractmethod
    def verify_classnote_upload_error(self):
        raise NotImplemented()

    @abstractmethod
    def upload_incorrect_format_class_note(self):
        raise NotImplemented()

    @abstractmethod
    def incorrect_note_format_error(self):
        raise NotImplemented()

    @abstractmethod
    def update_post_requisite_class_note(self, requisite_name, class_note_id):
        raise NotImplemented()

    @abstractmethod
    def uninstall_pdf_reader_apps(self):
        raise NotImplemented()

    @abstractmethod
    def install_app(self, apk):
        raise NotImplemented()

    @abstractmethod
    def install_pdf_reader_apps(self):
        raise NotImplemented()
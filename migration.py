import re
import sys
import glob
import os

if len(sys.argv) < 2:
    print('Please provide path to your project')
    sys.exit()
else:
    path = sys.argv[1]


for file in glob.glob(os.path.join(path, "**/*.*"), recursive=True):

    if not re.search(r"\.(html|scss|css|js|xml|po|pot)$", file):
        continue

    with open(file, 'r', encoding='utf-8') as source_file:
        content = source_file.read()

    re_group_first = r"(\s|\"|\[|\.)"

    if re.search(r"\.(scss|css)$", file):
        re_group_first = r"(\.)"

    # data-bs-
    content = re.sub(
        rf'{re_group_first}data-toggle=',
        r'\1data-bs-toggle=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-animation=',
        r'\1data-bs-animation=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-autohide=',
        r'\1data-bs-autohide=',
        content
    )
    if 'data-boundary' in content:
        content = re.sub(
            rf'{re_group_first}data-boundary=',
            r'\1data-bs-boundary=',
            content
        )
    content = re.sub(
        rf'{re_group_first}data-container=',
        r'\1data-bs-container=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-boundary=',
        r'\1data-bs-boundary=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-content=',
        r'\1data-bs-content=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-custom-class=',
        r'\1data-bs-custom-class=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-boundary=',
        r'\1data-bs-boundary=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-delay=',
        r'\1data-bs-delay=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-dismiss=',
        r'\1data-bs-dismiss=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-display=',
        r'\1data-bs-display=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-html=',
        r'\1data-bs-html=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-interval=',
        r'\1data-bs-interval=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-keyboard=',
        r'\1data-bs-keyboard=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-method=',
        r'\1data-bs-method=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-offset=',
        r'\1data-bs-offset=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-pause=',
        r'\1data-bs-pause=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-offset=',
        r'\1data-bs-offset=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-placement=',
        r'\1data-bs-placement=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-popper-config=',
        r'\1data-bs-popper-config=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-reference=',
        r'\1data-bs-reference=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-ride=',
        r'\1data-bs-ride=',
        content
    )
    # content = re.sub(
    #     rf'{re_group_first}data-selector=',
    #     r'\1data-bs-selector=',
    #     content
    # )
    content = re.sub(
        rf'{re_group_first}data-slide=',
        r'\1data-bs-slide=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-slide-to=',
        r'\1data-bs-slide-to=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-target=',
        r'\1data-bs-target=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-template=',
        r'\1data-bs-template=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-touch=',
        r'\1data-bs-touch=',
        content
    )
    content = re.sub(
        rf'{re_group_first}data-trigger=',
        r'\1data-bs-trigger=',
        content
    )

    # badges
    content = re.sub(
        rf'{re_group_first}badge-primary',
        r'\1text-bg-primary',
        content
    )
    content = re.sub(
        rf'{re_group_first}badge-secondary',
        r'\1text-bg-secondary',
        content
    )
    content = re.sub(
        rf'{re_group_first}badge-light',
        r'\1text-bg-light',
        content
    )
    content = re.sub(
        rf'{re_group_first}badge-danger',
        r'\1text-bg-danger',
        content
    )
    content = re.sub(
        rf'{re_group_first}badge-info',
        r'\1text-bg-info',
        content
    )
    content = re.sub(
        rf'{re_group_first}badge-success',
        r'\1text-bg-success',
        content
    )
    content = re.sub(
        rf'{re_group_first}badge-warning',
        r'\1text-bg-warning',
        content
    )
    content = re.sub(
        rf'{re_group_first}badge-dark',
        r'\1text-bg-dark',
        content
    )
    content = re.sub(
        rf'{re_group_first}badge-pill',
        r'\1rounded-pill',
        content
    )

    # border
    content = re.sub(
        rf'{re_group_first}border-left',
        r'\1border-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}border-right',
        r'\1border-end',
        content
    )

    # custom
    content = re.sub(
        rf'{re_group_first}custom-control-input',
        r'\1form-check-input',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-control-label',
        r'\1form-check-label',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-control custom-checkbox',
        r'\1form-check',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-control custom-radio',
        r'\1form-check',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-range',
        r'\1form-range',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-control-inline',
        r'\1form-check-inline',
        content
    )

    content = re.sub(
        rf'{re_group_first}custom-file-input',
        r'\1form-control',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-file-label',
        r'\1form-control',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-select-sm',
        r'\1form-select-sm',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-select-lg',
        r'\1form-select-lg',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-select',
        r'\1form-select',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-control custom-switch',
        r'\1form-check form-switch',
        content
    )
    content = re.sub(
        rf'{re_group_first}custom-control-inline',
        r'\1form-check-inline',
        content
    )
    # float
    content = re.sub(
        rf'{re_group_first}float-left',
        r'\1float-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}float-sm-left',
        r'\1float-sm-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}float-md-left',
        '\1float-md-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}float-lg-left',
        r'\1float-lg-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}float-xl-left',
        r'\1float-xl-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}float-right',
        r'\1float-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}float-sm-right',
        r'\1float-sm-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}float-md-right',
        r'\1float-md-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}float-lg-right',
        r'\1float-lg-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}float-xl-right',
        r'\1float-xl-end',
        content
    )
    # font
    content = re.sub(
        rf'{re_group_first}font-italic',
        r'\1fst-italic',
        content
    )
    content = re.sub(
        rf'{re_group_first}font-weight-bold',
        r'\1fw-bold',
        content
    )
    content = re.sub(
        rf'{re_group_first}font-weight-bolder',
        r'\1fw-bolder',
        content
    )
    content = re.sub(
        rf'{re_group_first}font-weight-light',
        r'\1fw-light',
        content
    )
    content = re.sub(
        rf'{re_group_first}font-weight-lighter',
        r'\1fw-lighter',
        content
    )
    content = re.sub(
        rf'{re_group_first}font-weight-normal',
        r'\1fw-normal',
        content
    )
    content = re.sub(
        rf'{re_group_first}font-weight-bold',
        r'\1fw-bold',
        content
    )
    content = re.sub(
        rf'{re_group_first}form-control-range',
        r'\1form-range',
        content
    )
    content = re.sub(
        rf'{re_group_first}form-control-file',
        r'\1form-control',
        content
    )
    content = re.sub(
        rf'{re_group_first}form-group',
        r'\1mb-3',
        content
    )
    content = re.sub(
        rf'{re_group_first}form-row',
        r'\1row',
        content
    )

    content = re.sub(
        rf'{re_group_first}jumbotron-fluid',
        r'\1rounded-0 px-0',
        content
    )
    content = re.sub(
        rf'{re_group_first}media-body',
        r'\1flex-grow-1',
        content
    )

    content = re.sub(
        rf'{re_group_first}ml-',
        r'\1ms-',
        content
    )
    content = re.sub(
        rf'{re_group_first}ml-n',
        r'\1ms-n',
        content
    )
    content = re.sub(
        rf'{re_group_first}mr-',
        r'\1me-',
        content
    )
    content = re.sub(
        rf'{re_group_first}mr-n',
        r'\1me-n',
        content
    )
    content = re.sub(
        rf'{re_group_first}no-gutters',
        r'\1g-0',
        content
    )
    content = re.sub(
        rf'{re_group_first}pl-',
        r'\1ps-',
        content
    )
    content = re.sub(
        rf'{re_group_first}pr-',
        r'\1pe-',
        content
    )
    content = re.sub(
        rf'{re_group_first}rounded-left',
        r'\1rounded-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}rounded-lg',
        r'\1rounded-3',
        content
    )
    content = re.sub(
        rf'{re_group_first}rounded-sm',
        r'\1rounded-1',
        content
    )
    content = re.sub(
        rf'{re_group_first}rounded-right',
        r'\1rounded-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-hide',
        r'\1d-none',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-left',
        r'\1text-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-sm-left',
        r'\1text-sm-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-md-left',
        r'\1text-md-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-lg-left',
        r'\1text-lg-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-xl-left',
        r'\1text-xl-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-right',
        r'\1text-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-sm-right',
        r'\1text-sm-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-md-right',
        r'\1text-md-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-lg-right',
        r'\1text-lg-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-xl-right',
        r'\1text-xl-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}text-monospace',
        r'\1font-monospace',
        content
    )

    #
    content = re.sub(
        r'<span aria-hidden="true">&times;</span>',
        '',
        content
    )

    content = re.sub(
        rf'{re_group_first}embed-responsive-item\s*',
        r'\1',
        content
    )
    content = re.sub(
        rf'{re_group_first}embed-responsive-16by9(\s|\"|\[|\.)',
        r'\1ratio-16x9',
        content
    )
    content = re.sub(
        rf'{re_group_first}embed-responsive-1by1',
        r'\1ratio-1x1',
        content
    )
    content = re.sub(
        rf'{re_group_first}embed-responsive-21by9',
        r'\1ratio-21x9',
        content
    )
    content = re.sub(
        rf'{re_group_first}embed-responsive-4by3',
        r'\1ratio-4x3',
        content
    )
    content = re.sub(
        rf'{re_group_first}embed-responsive',
        r'\1ratio',
        content
    )

    content = re.sub(
        rf'{re_group_first}dropdown-menu-left',
        r'\1dropdown-menu-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropdown-menu-sm-left',
        r'\1dropdown-menu-sm-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropdown-menu-md-left',
        r'\1dropdown-menu-md-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropdown-menu-lg-left',
        r'\1dropdown-menu-lg-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropdown-menu-xl-left',
        r'\1dropdown-menu-xl-start',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropdown-menu-right',
        r'\1dropdown-menu-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropdown-menu-sm-right',
        r'\1dropdown-menu-sm-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropdown-menu-md-right',
        r'\1dropdown-menu-md-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropdown-menu-lg-right',
        r'\1dropdown-menu-lg-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropdown-menu-xl-right',
        r'\1dropdown-menu-xl-end',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropleft',
        r'\1dropstart',
        content
    )
    content = re.sub(
        rf'{re_group_first}dropright',
        r'\1dropend',
        content
    )

    content = re.sub(
        rf'{re_group_first}sr-only-focusable',
        r'\1visually-hidden-focusable',
        content
    )
    content = re.sub(
        rf'{re_group_first}sr-only',
        r'\1visually-hidden',
        content
    )
    content = re.sub(
        rf'{re_group_first}sr-only-focusable',
        r'\1visually-hidden-focusable',
        content
    )

    with open(file, 'w', encoding='utf-8') as source_file:
        source_file.write(content)

print('Done!!')

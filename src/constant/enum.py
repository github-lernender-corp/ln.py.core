from enum import Enum, auto

class HelpType(Enum):
    Undefined = 0
    Default = 1
    Information = 2
    Warning = 3
    Error = 4

class ListboxType(Enum):
    Undefined = 0
    Standard = 1
    Checkbox = 2
    MultiSelect = 3
    Folder = 4

class EventType(Enum):
    Undefined = 0    
    Add = 1
    Click = 2
    Delete = 3
    Edit = 4
    Informational = 5
    Notification = 6
    Pull = 7
    Push = 8
    Remove = 9
    Select = 10
    Warning = 11

class ConnectionState(Enum):
    Undefined = 0 
    Connecting = 0
    Open = 1
    Closing = 2
    Closed = 3
    Aborted = 4

class AddressType(Enum):
    Undefined = 0
    Business = 1
    Home = 2
    Other = 3
    Work = 4

class EmailType(Enum):
    Undefined = 0
    Business = 1
    Home = 2
    Other = 3
    Work = 4

class PhoneType(Enum):
    Undefined = 0
    Business = 1
    Home = 2
    Other = 3
    Work = 4
    Mobile = 5

class FileType(Enum):
    Undefined = 0
    MicrosoftWord = 0
    MicrosoftExcel = 1
    CSV = 2

class StatusType(Enum):
    Undefined = 0
    Active = 1
    InActive = 2

class Direction(Enum):
    Undefined = 0
    Ascending = 1
    Descending = 2


class SelectionType(Enum):
    Undefined = 0
    Single = 1
    MultiSelect = 2
    MultiChecked = 3


class Case(Enum):
    Undefined = 0
    Upper = 1
    Lower = 2
    Camel = 3
    Pascal = 4

class Layout(Enum):
    Undefined = 0
    Horizontal = 1
    Vertical = 2


class GridView(Enum):
    Undefined = 0
    Standard = 1
    Vertical = 2
    Horizontal = 3

class TableView(Enum):
    Undefined = 0
    Card = 1
    Table = 2

class WindowState(Enum):
    Undefined = 0
    Normal = 1
    Open = 2
    Closed = 3
    Minimized = 4
    Maximized = 5


class Dock(Enum):
    Undefined = 0
    Top = 1
    Bottom = 2
    Left = 3
    Right = 4


class Command(Enum):
    Undefined = 0
    Activated = 1
    Deactivated = 2
    Add = 3
    Edit = 4
    Delete = 5
    Search = 6
    Update = 7
    Revert = 8
    Download = 9
    View = 10
    OK = 11
    Cancel = 12

class ComponentType(Enum):
    Undefined = 0
    AppMenu = 1
    Banner = 2
    Button = 3
    Calendar = 4
    CalendarCard = 5
    Card = 6
    CardProfile = 7
    Category = 8
    Checkbox = 9
    Clock = 10
    Command = 11
    ComponentViewer = 12
    Currency = 13
    Date = 14
    DatePicker = 15
    DropDown = 16
    DropdownType = 17
    Footer = 18
    Header = 19
    Help = 20
    Hyperlink = 21
    Icon = 22
    Image = 23
    Json = 24
    Message = 25
    NavContainer = 26
    NavMenu = 27
    NavSideBar = 28
    Notification = 29
    Number = 30
    Pagination = 31
    Panel = 32
    Percent = 33
    RadioButton = 34
    Search = 35
    SearchGroup = 36
    Tab = 37
    TabContent = 38
    Table = 39
    TableFilter = 40
    TableFooter = 41
    TaskBar = 42
    Text = 43
    TextArea = 44
    ToolTip = 45
    Toolbar = 46
    TypeAhead = 47

class TimeoutDelay(Enum):
    Short = 10
    Medium = 100
    Long = 250

class Equality(Enum):
    Undefined = 0
    Equal = 1
    Not = 2
    Between = 3
    GreaterThan = 4
    GreaterThanOrEqual = 5
    LessThan = 6
    LessThanOrEqual = 7

class Checkbox(Enum):
    Undefined = 0
    Checked = 1
    Unchecked = 2
    Deselect = 3

class StackAction(Enum):
    Undefined = 0
    Init = 1
    Push = 2
    Pop = 3

class HttpType(Enum):
    Undefined = 0
    Error = 1
    Get = 2
    Post = 3
    Put = 4
    Patch = 5
    Delete = 6
    Request = 7
    Response = 8

class Title(Enum):
    Undefined = 0
    Mr = 1
    Mrs = 2
    Ms = 3
    Other = 4

__all__ = [
    AddressType,
    Case,
    Checkbox,
    Command,
    ComponentType,
    ConnectionState,
    Direction,
    Dock,
    EmailType,
    Equality,
    EventType,
    FileType,
    GridView,
    HelpType,
    HttpType,
    Layout,
    ListboxType,
    PhoneType,
    SelectionType,
    StackAction,
    StatusType,
    TableView,
    TimeoutDelay,
    Title,
    WindowState
]
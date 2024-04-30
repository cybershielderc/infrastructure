interface MenuItem {
    id: number;
    title: string;
    link: string;
    has_dropdown: boolean;
    sub_menus?: {
        link: string;
        title: string;
    }[];
}[];

const menu_data: MenuItem[] = [
    
    {
        id: 1,
        has_dropdown: false,
        title: "Home",
        link: "/",
    },
    {
        id: 2,
        has_dropdown: false,
        title: "Feature",
        link: "/#feature",
    },
    {
        id: 3,
        has_dropdown: false,
        title: "Ico Chart",
        link: "/#chart",
    },
    {
        id: 4,
        has_dropdown: false,
        title: "RoadMap",
        link: "/#roadMap",
    },
    {
        id: 5,
        has_dropdown: true,
        title: "Blog",
        link: "/blog",
        sub_menus: [
            { link: "/blog", title: "Our Blog" },
            { link: "/blog-details", title: "Blog-Details", },
        ],
    },
    {
        id: 6,
        has_dropdown: false,
        title: "Contact",
        link: "/contact",
    },
];
export default menu_data;

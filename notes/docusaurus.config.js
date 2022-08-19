// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

/** @type {import('@docusaurus/types').Config} */
const config = {
    title: "DSA",
    tagline: "DSA & System Design",
    url: "https://pauulontteri.com",
    baseUrl: "/dsa/",
    onBrokenLinks: "throw",
    onBrokenMarkdownLinks: "warn",
    favicon: "img/favicon.ico",

    // GitHub pages deployment config.
    // If you aren't using GitHub pages, you don't need these.
    organizationName: "paulonteri", // Usually your GitHub org/user name.
    projectName: "dsa", // Usually your repo name.

    // Even if you don't use internalization, you can use this field to set useful
    // metadata like html lang. For example, if your site is Chinese, you may want
    // to replace "en" with "zh-Hans".
    i18n: {
        defaultLocale: "en",
        locales: ["en"],
    },

    presets: [
        [
            "classic",
            /** @type {import('@docusaurus/preset-classic').Options} */
            ({
                docs: {
                    sidebarPath: require.resolve("./sidebars.js"),
                    routeBasePath: "/",
                    // Please change this to your repo.
                    // Remove this to remove the "edit this page" links.
                    editUrl:
                        "https://github.com/paulonteri/data-structures-and-algorithms/tree/master/notes/",
                },
                blog: false, // Optional: disable the blog plugin
                theme: {
                    customCss: require.resolve("./src/css/custom.css"),
                },
            }),
        ],
    ],

    themeConfig:
        /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
        ({
            navbar: {
                title: "DSA",
                logo: {
                    alt: "My Site Logo",
                    src: "img/logo.png",
                },
                items: [
                    {
                        to: "/ds&a/intro",
                        label: "Data Structures & Algos",
                        position: "left",
                    },
                    {
                        to: "/sys-design/intro",
                        label: "System Design",
                        position: "left",
                    },
                    {
                        href: "https://github.com/paulonteri/data-structures-and-algorithms",
                        label: "GitHub",
                        position: "right",
                    },
                ],
            },
            footer: {
                // style: "dark",
                links: [
                    {
                        title: "DSA",
                        items: [
                            {
                                to: "/ds&a/intro",
                                label: "Data Structures and Algorithms",
                            },
                            {
                                to: "/sys-design/intro",
                                label: "System Design",
                            },
                        ],
                    },
                    {
                        title: "Community",
                        items: [
                            {
                                label: "GitHub",
                                href: "https://github.com/paulonteri/data-structures-and-algorithms",
                            },
                            {
                                label: "Twitter",
                                href: "https://twitter.com/paulonteri",
                            },
                        ],
                    },
                    {
                        title: "More",
                        items: [
                            {
                                label: "Blog",
                                href: "https://paulonteri.com/thoughts",
                            },
                            {
                                label: "Projects",
                                href: "https://paulonteri.com/projects",
                            },
                        ],
                    },
                ],
                copyright: `Built with 💙 by Paul Onteri using Docusaurus.`,
            },
            prism: {
                theme: lightCodeTheme,
                darkTheme: darkCodeTheme,
            },
        }),
};

module.exports = config;

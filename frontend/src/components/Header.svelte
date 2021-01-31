<script>
  import {
    SkipToContent,
    Header,
    HeaderUtilities,
    HeaderGlobalAction,
  } from "carbon-components-svelte";
  import LogoGithub20 from "carbon-icons-svelte/lib/LogoGithub20";
  import HelpFilled20 from "carbon-icons-svelte/lib/HelpFilled20";
  import {getContext} from "svelte";
  import {asn, name} from "../stores";

  const ctx = getContext("Theme");

  $: if (ctx) {
    ctx.dark.subscribe((value) => {
      console.log("dark mode?", value);
    });
    ctx.light.subscribe((value) => {
      console.log("light mode?", value);
    });
    ctx.updateVar("--cds-productive-heading-06-font-size", "4rem");
  }
</script>

<Header company="IRR GUI" platformName="AS{$asn} {$name}" href="/">
  <div slot="skip-to-content">
    <SkipToContent />
  </div>
  <HeaderUtilities>
    <HeaderGlobalAction aria-label="API Docs" icon="{HelpFilled20}" on:click={() => window.location = "/redoc"}/>
    <HeaderGlobalAction aria-label="GitHub Repo" icon="{LogoGithub20}" on:click={() => window.location = "https://github.com/natesales/irr-gui"}/>
  </HeaderUtilities>
</Header>

module Jekyll
  module VersionSelector


    # Given a string input of "nightly", "stable", "legacy", or "doc",
    # outputs a formatted string that looks like one of the following
    # (where "0.xx" is a RAPIDS version):
    #  - "nightly (0.xx)"
    #  - "stable (0.xx)"
    #  - "legacy (0.xx)"
    # The "doc" input returns a string based on the document version
    # that the filter was used on.
    def version_selector(input)
      releases = @context.registers[:site].data["releases"]
      doc_version = get_doc_version(@context.registers[:page])

      if input === "nightly"
        version = releases["nightly"]["version"]
        return "nightly (#{version})"
      end

      if input === "stable"
        version = releases["stable"]["version"]
        return "stable (#{version})"
      end

      if input === "legacy"
        legacy_version = releases["legacy"]["version"]

        if is_very_old(legacy_version, doc_version)
          return "legacy (#{doc_version})"
        end
        return "legacy (#{legacy_version})"
      end

      if input === "doc"
        ["nightly", "stable", "legacy"].each do |term|
          term_version = releases[term]["version"]
          if doc_version == term_version
            return "#{term} (#{term_version})"
          end
        end

        return "legacy (#{doc_version})"
      end

      raise "'version_selector' filter only supports the following inputs: 'nightly', 'stable', 'legacy', 'doc'"
    end

    # Uses the filter input and document version to determine whether
    # or not an "active" class should be added to the menu item.
    def add_active_class(input)
      releases = @context.registers[:site].data["releases"]
      doc_version = get_doc_version(@context.registers[:page])
      active_class = "rapids-selector__menu-item--selected"
      return_str = ""

      if input === "stable"
        if doc_version === releases["stable"]["version"]
          return_str = active_class
        end
      end

      if input === "nightly"
        if doc_version === releases["nightly"]["version"]
          return_str = active_class
        end
      end

      if input === "legacy"
        legacy_version = releases["legacy"]["version"]

        if doc_version === releases["legacy"]["version"]
          return_str = active_class
        end
        if is_very_old(legacy_version, doc_version)
          return_str = active_class
        end
      end

      return return_str

    end

    private

    # Returns true if the doc_version is older than the current
    # RAPIDS legacy version
    def is_very_old(site_legacy, doc_version)
      site_num = Integer(site_legacy[2..])
      doc_num = Integer(doc_version[2..])
      return doc_num < site_num
    end

    # Gets the RAPIDS version number (i.e. "0.15") from the page
    # frontmatter or throws an error if it doesn't exist
    def get_doc_version(page_obj)
      doc_version = page_obj["doc_version"]

      if doc_version
        return doc_version
      end
      raise "Couldn't find RAPIDS version number in page frontmatter"
    end
  end
end

Liquid::Template.register_filter(Jekyll::VersionSelector)
